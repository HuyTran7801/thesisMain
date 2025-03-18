from database.dbCon import *


class QuestionCourseDB:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        
    def create_question_course(self, question_id, course_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       insert into thesis.question_course (question_id, course_id) values
                       (%s, %s)
                       """, (question_id, course_id))
        self.__conn.commit()
        
    