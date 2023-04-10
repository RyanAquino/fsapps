import requests
from dts_models import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

def create_object(item):
    data_obj = None
    table_nbr = item['table_nbr'].replace("-","").upper()

    if table_nbr == "I":
        data_obj = DTS_Table_1(**item)
    elif table_nbr == "II":
        data_obj = DTS_Table_2(**item)
    elif table_nbr == "IIIA":
        data_obj = DTS_Table_3a(**item)
    elif table_nbr == "IIIB":
        data_obj = DTS_Table_3b(**item)
    elif table_nbr == "IIIC":
        data_obj = DTS_Table_3c(**item)
    elif table_nbr == "IV":
        data_obj = DTS_Table_4(**item)
    elif table_nbr == "V":
        data_obj = DTS_Table_5(**item)
    elif table_nbr == "VI":
        data_obj = DTS_Table_6(**item)

    return data_obj

def get_data_per_date(table, date):
    base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    endpoint = f"v1/accounting/dts/{table}"
    param = f"filter=record_date:eq:{date}"
    
    result = requests.get(f"{base_url}/{endpoint}?{param}").json()

    for data in result['data']:
        yield create_object(data)

    if result['meta']['total-pages'] > 1:
        get_data_per_date(table, date+result['links']['next'])

def insert(data_obj_list):
    session = Session()

    try:
        session.bulk_save_objects(data_obj_list)
        session.commit()
        print(f"Save and commit changes to database done.")

    except Exception as error:
        session.rollback()
        raise

    finally:
        session.close()

def get_first_record_date(table):
    api = f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/{table}?sort=-record_date&page%5Bsize%5D=1"

    result = requests.get(api).json()['data']
    return result[0]['record_date'] if len(result) == 1 else None

def main():
    date = "2005-10-03"

    dts_tables = [
        "dts_table_1",
        "dts_table_2",
        "dts_table_3a",
        "dts_table_3b",
        "dts_table_3c",
        "dts_table_4",
        "dts_table_5",
        "dts_table_6",
    ]

    for table in dts_tables:
        record_date = get_first_record_date(table)
        data_obj_list = [item for item in get_data_per_date(table, record_date)]

        print(f"Inserting {table} to database for date {record_date}.")
        insert(data_obj_list)

if __name__ == "__main__":
    main()