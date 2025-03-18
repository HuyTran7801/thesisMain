from database.dbCon import *


class RoleDB:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        
    def get_role_by_name(self, rolename):
        cursor= self.__conn.cursor()
        cursor.execute("""
                       select * from thesis.role r
                       where r.role = %s
                       """, (rolename,))
        return cursor.fetchone()
    
    def get_role_by_id(self, role_id):
        cursor= self.__conn.cursor()
        cursor.execute("""
                       select * from thesis.role r
                       where r.id = %s
                       """, (role_id,))
        return cursor.fetchone()