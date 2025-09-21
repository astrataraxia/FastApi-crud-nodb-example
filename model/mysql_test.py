import mysql.connector

from mysql.connector import Error
from config import config

def list_admin():
    with mysql.connector.connect(**config.MYSQL_DB_CONFIG) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM TB_ADMIN")
            results = cursor.fetchall()
        except Error as err:
            print("쿼리 에러: {err}" )
            results = False
    return results