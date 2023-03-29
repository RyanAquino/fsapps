import mysql.connector
from mysql.connector import Error


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

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def insert_data(result, source):
    connection = create_server_connection("localhost", "root", "", "fsapps")
    count = 0

    for key, val in result.items():
        table = key
        for i in val:
            key = list(i.keys())[0]
            i[key].insert(0, key)
            i[key].insert(0, table)
            i[key].insert(0, source)
            fill = ['NULL'] * (8-len(i[key]))
            i[key].extend(fill)
            
            query = f"INSERT INTO data VALUES {tuple(i[key])}".replace("'NULL'", 'NULL')
            execute_query(connection, query)
            count+=1
    return f"{count} rows inserted."