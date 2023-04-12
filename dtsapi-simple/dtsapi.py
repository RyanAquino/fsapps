"""DTS Script main module."""
import time

import requests
import schedule
from dts_models import (
    Base,
    DTS_Table_1,
    DTS_Table_2,
    DTS_Table_3a,
    DTS_Table_3b,
    DTS_Table_3c,
    DTS_Table_4,
    DTS_Table_5,
    DTS_Table_6,
    init_db,
)
from sqlalchemy.orm import Session, sessionmaker


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
    param = f"filter=record_date:gte:{date}"
    print(f"Sending request: {base_url}/{endpoint}?{param}")
    response = requests.get(f"{base_url}/{endpoint}?{param}", timeout=60).json()

    results += response.get("data")

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
        print("Done!! Saved and committed changes to database.")

    except Exception as error:
        session.rollback()
        print(error)
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


def get_first_record_date(table: str) -> str:
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

    result = requests.get(api, timeout=60).json()["data"]
    return result[0]["record_date"] if len(result) == 1 else None


def job(session: Session):
    """
    Main job that retrieves data for all DTS tables.

    :param session: Session object
    :return: None
    """
    dts_tables = {
        "I": DTS_Table_1,
        "II": DTS_Table_2,
        "IIIA": DTS_Table_3a,
        "IIIB": DTS_Table_3b,
        "IIIC": DTS_Table_3c,
        "IV": DTS_Table_4,
        "V": DTS_Table_5,
        "VI": DTS_Table_6,
    }

    for table_obj in dts_tables.values():
        table_name = table_obj.__name__
        table_lowered = table_name.lower()
        record_date = get_first_record_date(table_lowered)
        exists = check_date_exists(table_obj, record_date, session)
        table_v_exists = table_lowered == "dts_table_6" and check_date_exists(
            DTS_Table_5, record_date, session
        )

        if exists or table_v_exists:
            print(f"Skipping!! data exists for date {record_date} on {table_lowered}.")
            continue

        data_table = get_data_per_date(table_lowered, record_date)
        data_objs = []

        # Map tables / special case for table data not in requested table API
        for item in data_table:
            table_model = dts_tables[item.get("table_nbr")]
            data_objs.append(table_model(**item))

        print(f"Inserting {table_name} to database for date {record_date}.")
        insert(data_objs, session)


def main(session: Session):
    """
    Main function that schedules the job every weekdays at 4:01 PM
    :param session: Session object
    :return: None
    """
    run_time = "16:01"

    schedule.every().monday.at(run_time).do(job, session)
    schedule.every().tuesday.at(run_time).do(job, session)
    schedule.every().wednesday.at(run_time).do(job, session)
    schedule.every().thursday.at(run_time).do(job, session)
    schedule.every().friday.at(run_time).do(job, session)

    while True:
        next_run = schedule.idle_seconds()
        print(f"Time till next run {time.strftime('%H:%M:%S', time.gmtime(next_run))}.")

        if next_run > 0:
            time.sleep(next_run)

        schedule.run_pending()


if __name__ == "__main__":
    db_engine = init_db()
    Session = sessionmaker(bind=db_engine)
    with Session() as db_session:
        main(db_session)
