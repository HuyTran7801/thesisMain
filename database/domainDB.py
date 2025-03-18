from database.dbCon import *


class DomainDB:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        
    def create_domain(self, domain, course_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                        INSERT INTO thesis.domain (domain, course_id)
                        SELECT %s, %s
                        WHERE NOT EXISTS (
                        SELECT 1 FROM thesis.domain d WHERE d.domain=%s)
                       """, (domain, course_id, domain))
        self.__conn.commit()
        
    def get_all_domains(self, course_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       select d.domain from thesis.domain d, thesis.course c
                       where c.id=d.course_id and c.id=%s
                       """, (course_id,))
        return cursor.fetchall()
    
    def get_domain(self, domain):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       select * from thesis.domain d where d.domain = %s
                       """, (domain, ))
        return cursor.fetchone()
    