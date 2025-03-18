from database.dbCon import *

class UserDB:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        
    def get_user(self, username, role):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       select u.id, r.role
                       from thesis.user u, thesis.role r
                       where u.name = %s and u.role_id = r.id
                       and r.role = %s
                       """, (username, role))
        return cursor.fetchone()
    
    def create_user(self, username, password, role_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       insert into thesis.user (name, password, role_id) values
                       (%s, %s, %s)
                       """, (username, password, role_id))
        self.__conn.commit()
        
    def check_exist_user(self, username):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       select * from thesis.user u
                       where u.name = %s
                       """,(username,))
        return cursor.fetchone()
        