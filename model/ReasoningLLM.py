from model.api_token import *
from mistralai import Mistral

# model = 'open-mistral-nemo'
model = 'mistral-large-2411'
# model_code = 'codestral-2501'

class ReasoningLLM:
    def __init__(self):
        self.llm = Mistral(api_key=HUGGINGFACEHUB_API_TOKEN)
        
    def generate_hard_MCQ(self, title):
        response = self.llm.chat.complete(
            model=model,
            messages=[
                {"role": "user",
                 "content": f"{title}"},
            ]
        )
        return response.choices[0].message.content