from model.RAG import *
from model.MultiAgentDebate import *


rag = RAG('./data/oop/user1')

multi_agent = MultiAgent()

context, docs = rag.semantic_search('Graph', 3)

multi_agent.generate_hard_MCQs('Data Structure and Algorithms', 20, context, 'Graph')

print('---FINAL MCQS---')
print(multi_agent.get_MCQs())