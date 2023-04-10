import requests
from dts_models import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

def get_data_per_date(table, date):
    base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    endpoint = f"v1/accounting/dts/{table}"
    param = f"filter=record_date:eq:{date}"
    
    result = requests.get(f"{base_url}/{endpoint}?{param}").json()

    for data in result['data']:
        yield data

    if result['meta']['total-pages'] > 1:
        get_data_per_date(table, date+result['links']['next'])

def insert(data_obj_list):
    session = Session()

    try:
        session.bulk_save_objects(data_obj_list)
        session.commit()
        print(f"Done!! Saved and committed changes to database.")

    except Exception as error:
        session.rollback()
        print(error)
        raise

    finally:
        session.close()

def check_date_exists(table, record_date):
    session = Session()

    try:
        exists = session.query(table).filter(table.record_date == record_date).count()

    except Exception as error:
        raise

    finally:
        session.close()
    
    return True if exists > 1 else False

def get_first_record_date(table):
    api = f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/{table}?sort=-record_date&page%5Bsize%5D=1"

    result = requests.get(api).json()['data']
    return result[0]['record_date'] if len(result) == 1 else None

def main():
    dts_tables = [
        "DTS_Table_1",
        "DTS_Table_2",
        "DTS_Table_3a",
        "DTS_Table_3b",
        "DTS_Table_3c",
        "DTS_Table_4",
        "DTS_Table_5",
        "DTS_Table_6",
    ]

    for table in dts_tables:
        record_date = get_first_record_date(table.lower())
        exists = check_date_exists(eval(table), record_date)
        table_obj = eval(table)
        if not exists:
            data_obj_list = [table_obj(**item) for item in get_data_per_date(table.lower(), record_date)]

            print(f"Inserting {table} to database for date {record_date}.")
            insert(data_obj_list)
        else:
            print(f"Skipping!! data exists for date {record_date} on {table.lower()}.")
            continue

if __name__ == "__main__":
    main()