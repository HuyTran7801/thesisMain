from model.api_token import *
from mistralai import Mistral


model_code = 'codestral-2501'

class CodingLLM:
    def __init__(self):
        self.llm = Mistral(api_key=HUGGINGFACEHUB_API_TOKEN)
        
    def generate_code(self):
        response = self.llm.chat.complete(
            model=model_code,
            messages=[
                {'role': 'user', 
                 'content':"Hi"},
            ]
        )
        return response.choices[0].message.content