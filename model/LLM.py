from mistralai import Mistral
from model.api_token import *

model = 'open-mistral-nemo'
model2 = 'mistral-large-2411'
model_code = 'codestral-2501'


class LLM:
    def __init__(self):
        self.llm = Mistral(api_key=HUGGINGFACEHUB_API_TOKEN)
        
    def generate_MCQ_RAG(self, title, rag, k_relevant):
        context, docs = rag.semantic_search(title, k_relevant)
        print('Docs:', docs)
        print('Context:', context)
        chat_response = self.llm.chat.complete(
            model = model,
            messages = [
                {
                    "role": "user",
                    "content": f"""
                    You are a role of an expert in Computer Science.
                    I need you help me in domain of {title}
                    Here is a context: 
                    ------------------------------
                    {context}
                    ------------------------------
                    . Then combine context with your knowledge from Wikipedia about this title.
                    Generate to me 5 MCQs relate to it. Don't show the answers""",
                },
            ]
        )
        return chat_response.choices[0].message.content
    
    def list_topics(self, title):
        chat_response = self.llm.chat.complete(
            model = model,
            messages = [
                {
                    "role": "user",
                    "content": f"""
                    You are a role of an expert in Computer Science.
                    Can you list me 10 topics in this {title}?
                    .Just print title-name of each topic, split them by comma""",
                },
            ]
        )
        return chat_response.choices[0].message.content