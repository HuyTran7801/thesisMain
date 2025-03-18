from model.ReasoningLLM import *
from model.Handling import *
from model.RAG import *


rag = RAG('./data/oop/user1')

docs = rag.load_documents('./static/files1')
chunks = rag.split_documents(docs)

context = ''
for i in chunks:
    val = i.page_content
    context += val

llm = ReasoningLLM('Object Oriented Programming', context)

mcqs = llm.generate_MCQs_RAG()

print(mcqs)

llm.system_prompt += 'Assistant: ' + mcqs
llm.system_prompt += f"""
User: I have wrong answers with questions 1, 3, 5, 6, 2, 7, 9.
Now you continue generate 10 MCQs which most of them are same to above questions
to help me improving my weakness, each question must contains 4 options.
. Don't show the answers
"""
# llm.system_prompt += f"""
# User: Now you continue generate 10 MCQs with more difficult than previous, each question must
# contains 4 options.
# Start each question number with 1., 2., ..., 10.
# Start answer with pattern 'A)', 'B)', 'C)', 'D)'
# . Don't show the answers
# """

mcqs_2 = llm.generate_MCQs_RAG()
print(mcqs_2)
