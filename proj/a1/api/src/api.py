"""DTS Script main module."""

import time
from typing import Optional, Callable

import requests
import schedule
import sqlalchemy.orm.session
from loguru import logger
from pytz import timezone
from sqlalchemy.orm import Session, sessionmaker

from aaii_live_scraper import main as aaii_live_job_scraper
from spy_finance_live_scraper import main as spy_finance_live_job_scraper
from models import (
    Adjustment_Public_Debt_Transactions_Cash_Basis,
    Base,
    Debt_Subject_To_Limit,
    Deposits_Withdrawals_Operating_Cash,
    Federal_Tax_Deposits,
    Income_Tax_Refunds_Issued,
    Inter_Agency_Tax_Transfers,
    Operating_Cash_Balance,
    Public_Debt_Transactions,
    Short_Term_Cash_Investments,
    init_db,
)


def get_data_per_date(table: str, date: str, date_orig=None, results=None):
    """
    Recursively retrieve data per date and table on DTS API.

    :param results:
    :param date_orig: date original
    :param table: table name
    :param date: date to be retrieved
    :return: all results
    """
    if not results:
        results = []

    base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    endpoint = f"v1/accounting/dts/{table}"
    param = f"filter=record_date:{date}"
    logger.info(f"Sending request: {base_url}/{endpoint}?{param}")

    try:
        response = requests.get(f"{base_url}/{endpoint}?{param}").json()
        results += response.get("data")
    except requests.exceptions.RequestException:
        logger.warning("Exception raised when sending HTTP requests")
        return results

    if response.get("meta").get("count") > 1 and (
        nxt := response.get("links").get("next")
    ):
        if not date_orig:
            date_orig = date

        return get_data_per_date(table, date_orig + nxt, date_orig, results)
    return results


def insert(data_obj_list: list, session: Session):
    """
    Bulk insert data per table.

    :param data_obj_list: list of data
    :param session: Session object
    :return: None
    """
    try:
        session.bulk_save_objects(data_obj_list)
        session.commit()
        logger.info("Done!! Saved and committed changes to database.")

    except Exception as error:
        session.rollback()
        logger.error(error)
        raise error


def check_date_exists(table: Base, record_date: str, session: Session) -> bool:
    """
    Check data exists by querying date.

    :param table: table object
    :param record_date: record date string
    :param session: Session object
    :return: True if existing else False
    """
    try:
        exists = session.query(table).filter(table.record_date == record_date).count()
    except Exception as error:
        raise error

    return exists > 1


def get_last_record_date(table: Base, session: Session) -> str:
    """
    Check data exists by querying date.

    :param table: table object
    :param session: Session object
    :return: Last inserted record_date
    """
    try:
        last_inserted = session.query(table).order_by(table.id.desc()).first()
    except Exception as error:
        raise error

    return last_inserted.record_date if last_inserted else None


def get_first_record_date(table: str) -> Optional[str]:
    """
    Retrieve latest record per table via API.

    :param table: table name
    :return: date string or None
    """
    api = (
        "https://api.fiscaldata.treasury.gov/services/"
        f"api/fiscal_service/v1/accounting/dts/{table}?"
        "sort=-record_date&page%5Bsize%5D=1"
    )

    try:
        result = requests.get(api).json()["data"]
    except requests.exceptions.RequestException:
        logger.warning("Exception raised when sending HTTP requests")
        return None

    return result[0]["record_date"] if len(result) == 1 else None


def dts_scraper(session: Session):
    """
    Main job that retrieves data for all DTS tables.

    :param session: Session object
    :return: None
    """
    dts_tables = {
        "Operating Cash Balance": Operating_Cash_Balance,
        "Deposits and Withdrawals of Operating Cash": Deposits_Withdrawals_Operating_Cash,
        "Public Debt Transactions": Public_Debt_Transactions,
        "Adjustment of Public Debt Transactions to Cash Basis": Adjustment_Public_Debt_Transactions_Cash_Basis,
        "Debt Subject to Limit": Debt_Subject_To_Limit,
        "Inter-agency Tax Transfers": Inter_Agency_Tax_Transfers,
        "Income Tax Refunds Issued": Income_Tax_Refunds_Issued,
        "Federal Tax Deposits": Federal_Tax_Deposits,
        "Short-Term Cash Investments": Short_Term_Cash_Investments,
    }

    for table_obj in dts_tables.values():
        table_name = table_obj.__name__
        table_lowered = table_name.lower()
        record_date = get_first_record_date(table_lowered)

        if not record_date:
            logger.warning(f"Temporary skipping {table_lowered}: API not available")
            continue

        exists = check_date_exists(table_obj, record_date, session)
        # table_v_exists = table_lowered == "b001b_dts_table_6" and check_date_exists(
        #     DTS_Table_5, record_date, session
        # )
        #

        if exists:
            logger.warning(
                f"Skipping!! data exists for date {record_date} on {table_lowered}."
            )
            continue

        # record_date = f"gt:2024-01-01"
        if last_record_date := get_last_record_date(table_obj, session):
            record_date = f"gt:{last_record_date}"
        else:
            record_date = f"eq:{record_date}"

        data_table = get_data_per_date(
            table_lowered, record_date + "&page%5Bsize%5D=10000"
        )
        data_objs = []

        # Map tables / special case for table data not in requested table API
        for item in data_table:
            table_model = dts_tables[item.get("table_nm")]
            data_objs.append(table_model(**item))

        logger.info(f"Inserting {table_name} to database for date {record_date}.")
        insert(data_objs, session)


def job_wrapper(job: Callable, session: sqlalchemy.orm.session.sessionmaker):
    """
    Wraps job with dependencies needed to instantiate every call.

    :param job: job func
    :param session: DB session maker
    :return: None
    """
    with session() as db_session:
        job(db_session)


def main(database_engine):
    """
    Main function that schedules the job every week days at 4:01 PM
    using New York time zone.
    :return: None
    """
    run_time = "16:01"
    time_zone = timezone("America/New_York")

    Session = sessionmaker(bind=database_engine)
    daily_jobs = [aaii_live_job_scraper, spy_finance_live_job_scraper]

    schedule.every().day.at(run_time, time_zone).do(job_wrapper, dts_scraper, Session)

    for job in daily_jobs:
        schedule.every(4).hours.do(job_wrapper, job, Session)

    while True:
        next_run = schedule.idle_seconds()
        logger.info(
            f"Time till next run {time.strftime('%H:%M:%S', time.gmtime(next_run))}."
        )

        if next_run > 0:
            time.sleep(next_run)

        schedule.run_pending()


if __name__ == "__main__":
    db_engine = init_db()
    main(db_engine)
