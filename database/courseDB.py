from database.dbCon import *

class CourseDB:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        
    def get_all_courses(self):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       select * from thesis.course
                       """)
        return cursor.fetchall()
    
    def create_course(self, course, code):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       insert into thesis.course (course_name, code) values
                       (%s,%s)
                       """,(course, code))
        self.__conn.commit()
        
    def get_course(self, course_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       select c.course_name, c.code 
                       from thesis.course c
                       where c.id = %s
                       """, (course_id,))
        return cursor.fetchone()
    
    def delete_course(self, course_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       delete from thesis.course c
                       where c.id = %s
                       """, (course_id,))
        self.__conn.commit()    