from model.RAG import *


rag = RAG('./data/oop/user1')

context, docs = rag.advanced_semantic_search('Inheritance', 50)

print(context)

print('--------')
print(docs)