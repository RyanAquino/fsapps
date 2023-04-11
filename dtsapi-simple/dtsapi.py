"""DTS Script main module."""
import time

import requests
import schedule
from sqlalchemy.orm import Session, sessionmaker
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


def get_data_per_date(table: str, date: str):
    """
    Retrieve data per date on DTS API.

    :param table: table name
    :param date: date to be retrieved
    :return: yielded data
    """
    base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    endpoint = f"v1/accounting/dts/{table}"
    param = f"filter=record_date:eq:{date}"

    result = requests.get(f"{base_url}/{endpoint}?{param}", timeout=60).json()

    for data in result["data"]:
        yield data

    if result["meta"]["total-pages"] > 1:
        get_data_per_date(table, date + result["links"]["next"])


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
    dts_tables = [
        DTS_Table_1,
        DTS_Table_2,
        DTS_Table_3a,
        DTS_Table_3b,
        DTS_Table_3c,
        DTS_Table_4,
        DTS_Table_5,
        DTS_Table_6,
    ]

    for table_obj in dts_tables:
        table_name = table_obj.__name__
        table_lowered = table_name.lower()
        record_date = get_first_record_date(table_lowered)
        exists = check_date_exists(table_obj, record_date, session)

        if not exists:
            data_obj_list = [
                table_obj(**item)
                for item in get_data_per_date(table_lowered, record_date)
            ]

            print(f"Inserting {table_name} to database for date {record_date}.")
            insert(data_obj_list, session)
        else:
            print(f"Skipping!! data exists for date {record_date} on {table_lowered}.")
            continue


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
