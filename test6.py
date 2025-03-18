from model.RAG import *
from model.MultiAgentDebate import *

rag = RAG('./data/oop/user1')

multi_agent = MultiAgent()

context, docs = rag.semantic_search('Graph', 3)

print('context')
print(context)
print('----------')

multi_agent.generate_MCQs('Data structure and Algorithm', 20, context, 'Graph')

print('---final mcqs---')
print(multi_agent.get_MCQs())