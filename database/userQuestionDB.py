from database.dbCon import *

class UserQuestionDB:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        
    def create_user_question(self, user_id, question_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       insert into thesis.user_question (user_id, question_id)
                       select %s, %s
                       where not exists (
                           select 1 from thesis.user_question uq where uq.question_id = %s
                       )
                       """, (user_id, question_id, question_id))
        self.__conn.commit()
        
    def delete_user_question(self, id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       delete from thesis.user_question uq where uq.id = %s
                       """, (id,))
        self.__conn.commit()
        
    def delete_all(self):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       delete from thesis.user_question
                       """)
        self.__conn.commit()
        
    def get_user_question(self, user_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       select q.id, q.question, q.label1, q.label2, q.label3, q.label4, q.answer, q.explanation, q.appear
                       from thesis.question q, thesis.user_question uq
                       where uq.user_id=%s and q.id = uq.question_id
                       """, (user_id,))
        return cursor.fetchall()
    
    def get_question_occurence(self, question_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       select * from thesis.user_question uq
                       where uq.question_id = %s
                       """, (question_id,))
        return cursor.fetchall()