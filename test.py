from model.RAG import *
from model.LLM import *
from model.ReasoningLLM import *
from model.Directory import *
from model.Handling import *
import os

rag = RAG('./data/oop/user1')

context, docs = rag.advanced_semantic_search('abstraction', 50)

# print(docs)
# # print('type 1', type(docs))
# print(len(docs))

docs = docs.replace('static\\\\filestemp1\\\\',' - ')
print(docs, ' ', type(docs))