import requests

from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, Integer, String



engine = create_engine("mysql+pymysql://root:@localhost/fsappsv2",echo = False)
metadata = MetaData()

def get_fields():
    url = "https://fiscaldata.treasury.gov/page-data/datasets/daily-treasury-statement/page-data.json"

    for i in requests.get(url).json()['result']['pageContext']['config']['apis']:
        yield i
    
def create_table_definition():
    database_dict = {}

    for api in get_fields():
        table = api['tableName'].replace(" ", "").replace("-","")
        database_dict[table] = { field['columnName']: "String(200)" 
                                 for field in api['fields']}
    
    return database_dict

    
def create_db():
    for table_name, table_data in create_table_definition().items():
        columns = [Column(column_name, eval(column_type)) for column_name, column_type in table_data.items()]
        table = Table(table_name, metadata, *columns)
        table.create(engine, checkfirst=True)

    return metadata


