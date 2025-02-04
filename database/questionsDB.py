from dbCon import *

class questionsDB:
    def __init__(self):
        self.conn = DBConnection().get_connection()
        
    def get_questions(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM thesis.questions")
        return cursor.fetchall()
    
    def create_question(self, mcq):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO thesis.questions (mcq, fail_attempt) VALUES (%s)", (mcq, 0))
        self.conn.commit()
        
    def update_fail_attempt(self, question_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE thesis.questions SET fail_attempt = fail_attempt + 1 WHERE id = %s", (question_id,))
        self.conn.commit()
        
    def delete_question(self, question_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM thesis.questions WHERE id = %s", (question_id,))
        self.conn.commit()