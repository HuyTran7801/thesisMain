from database.questionsDB import *
from model.MultiAgentDebate import *

question_db = QuestionsDB()

questions = question_db.get_all_questions_with_topic('property of oop', 1, 15)

# print(questions)
questions_from_db = ''
for i in questions:
    # print(i)
    questions_from_db += i[1] + 'A) ' + i[2] + 'B) ' + i[3] + 'C) ' + i[4] + 'D) ' + i[5] + i[7]


# print(questions_from_db)

multi_agent = MultiAgent()

multi_agent.generate_more_MCQs('Object-oriented programming', questions_from_db, 3, '', 'property of OOP')
mcqs = multi_agent.get_MCQs()

print('----FINAL ANS----')
print(mcqs)
