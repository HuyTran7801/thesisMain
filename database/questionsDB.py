from database.dbCon import *

class QuestionsDB:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        
    
    def create_question(self, question, label1, label2, label3, label4, answer, explanation, appear, trial, level_id, domain_id):
        cursor = self.__conn.cursor()
        cursor.execute("""INSERT INTO thesis.question (question, label1, label2, label3, label4, answer, explanation, appear, trial, level_id, domain_id) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                       (question,label1, label2, label3, label4, answer, explanation, appear, trial, level_id, domain_id))
        self.__conn.commit()
        
    def update_fail_attempt(self, question_id):
        cursor = self.__conn.cursor()
        cursor.execute("UPDATE thesis.question SET trial = trial + 1 WHERE id = %s", (question_id,))
        self.__conn.commit()
        
    def update_appearance(self, question_id):
        cursor = self.__conn.cursor()
        cursor.execute("UPDATE thesis.question SET appear = appear + 1 WHERE id = %s", (question_id,))
        self.__conn.commit()
        
    def get_all_questions(self):
        cursor = self.__conn.cursor()
        cursor.execute("""select * from thesis.question""")
        return cursor.fetchall()
    
    def get_question(self, question_name):
        cursor = self.__conn.cursor()
        cursor.execute("""
                       select * from thesis.question q
                       where q.question = %s
                       """, (question_name,))
        return cursor.fetchone()
    
    def get_all_questions_with_topic(self, domain_name, level_id):
        cursor = self.__conn.cursor()
        cursor.execute("""
                        select q.id, q.question, q.label1, q.label2, q.label3, q.label4, q.answer, q.explanation, q.appear
                        from thesis.domain d, thesis.question q
                        where d.domain = %s and q.level_id = %s and d.id = q.domain_id
                       """, (domain_name, level_id))
        return cursor.fetchall()