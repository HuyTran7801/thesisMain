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
                 'content':"""
                    You are expert in Coding review. You have the abilities like coding, fixing bug and give me a test case.
                    Now let's check this code about function sum of elements of array:                 
                    def getSum(arr):
                        s = 0
                        for i in arr:
                            s += i
                        return s
                        
                    You must follow this pattern to evaluate:
                    1. First, give me 3 test cases and run the user's code with test case.
                    2. Finally, if it passes all test cases, print 'CORRECT', otherwise print 'INCORRECT'.
                 """},
            ]
        )
        return response.choices[0].message.content