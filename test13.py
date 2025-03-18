from model.Handling import *
from database.questionsDB import *
from model.MultiAgentDebate import *


question_db = QuestionsDB()
multi_agent=MultiAgent()

multi_agent.generate_MCQs('Object-oriented Programming', 5, '', 'Inheritance')
ans = multi_agent.get_MCQs()

mcqs = question_db.get_all_questions()
handling = Handling()

print('-----DB------')
for i in mcqs:
    print('Question :', i[1])
    
    print('A) ', i[2])
    print('B) ', i[3])
    print('C) ', i[4])
    print('D) ', i[5])
    
    print('Corrected answer: ', i[6])
    
    explanation = handling.split_explanation(i[7])
    print('Feedback 1: ', explanation[0])
    print('Feedback 2: ', explanation[1])    
    
    # print('Appear: ', i[8])
print('------------')

print('-----LLM-----')
ans_lst = handling.split_5_mcqs(ans)
for i in ans_lst:
    question, answer_lst, feedback_lst, corrected_ans = handling.split_QA(i)
    print('Question: ', question)
    
    print('A) ', answer_lst[0])
    print('B) ', answer_lst[1])
    print('C) ', answer_lst[2])
    print('D) ', answer_lst[3])
    
    print('Corrected answer: ', corrected_ans)
    
    print('Feedback 1: ', feedback_lst[0])
    print('Feedback 2: ', feedback_lst[1])
    
    
print('_________')