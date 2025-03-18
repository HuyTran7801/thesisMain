from model.api_token import *
from mistralai import Mistral
from google import genai

# model = 'open-mistral-nemo'
# model = 'mistral-large-2411'
# model_code = 'codestral-2501'


API='AIzaSyDHWooSXhFddX9WEIpQtbPqPv0ld2ws4m4'

class ReasoningLLM:
    def __init__(self):
        self.__client = genai.Client(api_key=API)
        self.__model = "gemini-1.5-pro"
    
    def generate_distractors(self, mcqs, num_of_mcqs, task):
        response = self.__client.models.generate_content(
            model = self.__model,
            contents=f"""
            You are an expert, outstanding professor in Computer Science.
            Here is the {num_of_mcqs} relate to {task} with difficult level.
            -------------------
            {mcqs}
            -------------------
            . Now your mission is:
                - Each question, you must print
            """
        )