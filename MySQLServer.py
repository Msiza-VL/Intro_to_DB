import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost'
}

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    create_database(cursor)
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
