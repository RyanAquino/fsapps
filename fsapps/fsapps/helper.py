import mysql.connector

from mysql.connector import Error
from create_db import create_db


def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(f"Error: '{err}'")

def read_query(query):
    connection = create_server_connection("localhost", "root", "", "fsapps")
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def normalize_table_data(data):
    raw = data.replace("—", " ").replace("–"," ").replace("-","").replace("º","").replace("]","")
    raw_data = ' '.join(raw.split())
    raw_data_list = raw_data.split(" ")
    
    # Handle roman numerals with l
    raw_data_list[1] = raw_data_list[1].replace("l","I")
    
    return raw_data_list

def insert_data(result, source):

    metadata = create_db()

    dts_table_1  = metadata.tables['OperatingCashBalance']
    dts_table_2  = metadata.tables['DepositsandWithdrawalsofOperatingCash']
    dts_table_3a = metadata.tables['PublicDebtTransactions']
    dts_table_3b = metadata.tables['AdjustmentofPublicDebtTransactionstoCashBasis']
    dts_table_3c = metadata.tables['DebtSubjecttoLimit']
    dts_table_4  = metadata.tables['FederalTaxDeposits']
    dts_table_5  = metadata.tables['ShortTermCashInvestments']
    dts_table_6  = metadata.tables['IncomeTaxRefundsIssued']

    # print(dts_table_1.c.keys())

    connection = create_server_connection("localhost", "root", "", "fsapps")
    count = 0

    for key, val in result.items():
        temp = normalize_table_data(key)
        # table = Table(table_nbr=temp[1], table_name= " ".join(temp[2:]))
        table = "".join(temp[2:])
        

        for i in metadata.tables:
            if i.startswith(table):
                print(i)

        # for i in val:
        #     key = list(i.keys())[0]
        #     i[key].insert(0, key)
        #     print(i[key])
            
        #     Data(
        #         record_date = "",
        #         account_type = key,
        #         close_today_bal = "",
        #         open_today_bal = "",
        #         open_month_bal= "",
        #         open_fiscal_year_bal= "",
        #         sub_table_name = "",
        #         src_line_nbr = "",
        #         record_fiscal_year = "",
        #         record_fiscal_quarter = "",
        #         record_calendar_year = "",
        #         record_calendar_quarter = "",
        #         record_calendar_month = "",
        #         record_calendar_day = "",
        #     )
    return
    
    #         query = f"INSERT INTO data VALUES {tuple(i[key])}".replace("'NULL'", 'NULL')
    #         execute_query(connection, query)
    #         count+=1
    # return f"{count} rows inserted."