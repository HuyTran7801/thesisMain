import mysql.connector 
from mysql.connector import Error

class DBConnection:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='giahuytran0708@',
                database='thesis'
            )
            print("Connection successful")
        except Error as e:
            print(f"Error: {e}")
            self.conn = None
        
    def get_connection(self):
        return self.conn
    