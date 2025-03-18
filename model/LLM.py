from mistralai import Mistral
from model.api_token import *

model = 'open-mistral-nemo'
model2 = 'mistral-large-2411'
model_code = 'codestral-2501'


class LLM:
    def __init__(self):
        self.__llm = Mistral(api_key='yTP3OlllcDaiqmgcoxJghetYuF9Z05fj')
        # self.__system_messages = []
    
    def generate_MCQs(self, title, context, num_of_mcqs, task):
        generate_prompt =  f"""
            You are an expert, a very outstanding professor in Computer Science.
            I need you help me in domain of {title}. 
            Use your knowledge to generate to me {num_of_mcqs} MCQs relate to {task}.
            Here is a context that support you to generate MCQs: 
            ------------------------------
            {context}
            ------------------------------
            . Note that if context is empty or not support enough information, you must use
            specific-domain knowledge to back up.
            . You must follow the pattern here:
                - Each question must contains 4 options.
                - Start each question number with 1., 2., etc.
                - Start answer with pattern 'A)', 'B)', 'C)', 'D)'.
                - Start the corrected answer with pattern 'The correct answer is: A), B), C) or D)' (note always print ')' after corrected option)
                - Start the explanation by 'Explanation:', you should explain why it is correct.
                - Start the reference by 'For more information:', you refer useful link relate to Computer Science
                as you know (GeeksForGeeks, Wikipedia, etc).
                    """
        response = self.__llm.chat.complete(
            model=model2,
            messages=[
                {
                    'role': 'user', 
                    'content': generate_prompt
                },
            ]
        )
        return response.choices[0].message.content
    
    def retake_MCQs(self, mcqs, wrong_questions, num_of_mcqs, task):
        generate_prompt = f"""
            You are an expert, a very outstanding professor in Computer Science.
            Here's all the previous MCQs relate to {task} that you generated before (delimited by ---------).
            -------------------
            {mcqs}
            -------------------
            . Student had wrong answers in question {wrong_questions}.
            To support student improve their weakness and retake the test
            . Now you generate {num_of_mcqs} MCQs again that review all {wrong_questions} wrong MCQs to encourage
            student's weakness.
            You must follow the pattern here:
                - Each question must contains 4 options.
                - Start each question number with 1., 2., etc.
                - Start answer with pattern 'A)', 'B)', 'C)', 'D)'.
                - Start the corrected answer with pattern 'The correct answer is: A), B), C) or D)' (note always print ')' after corrected option)
                - Start the explanation by 'Explanation:', you should explain why it is correct.
                - Start the reference by 'For more information:', you refer useful link relate to Computer Science
                as you know (GeeksForGeeks, Wikipedia, etc).
        """
        response = self.__llm.chat.complete(
            model=model2,
            messages=[
                {
                    'role': 'user', 
                    'content': generate_prompt
                },
            ]
        )
        return response.choices[0].message.content
    
    def level_up_MCQs(self, mcqs, num_of_mcqs, task):
        generate_prompt = f"""
            You are an expert, a very outstanding professor in Computer Science.
            Here's all the previous MCQs relate to {task} that you generated before (delimited by ---------).
            -------------------
            {mcqs}
            -------------------
            . Student had passed all the above multiple-choice questions well.
            To challenge student with more difficult level of multiple-choice questions.
            . Now you generate {num_of_mcqs} MCQs with difficult level than all previous.
            You must follow the pattern here:
                - Each question must contains 4 options.
                - Start each question number with 1., 2., etc.
                - Start answer with pattern 'A)', 'B)', 'C)', 'D)'.
                - Start the corrected answer with pattern 'The correct answer is: A), B), C) or D)' (note always print ')' after corrected option)
                - Start the explanation by 'Explanation:', you should explain why it is correct.
                - Start the reference by 'For more information:', you refer useful link relate to Computer Science
                as you know (GeeksForGeeks, Wikipedia, etc).
        """
        response = self.__llm.chat.complete(
            model=model2,
            messages=[
                {
                    'role': 'user', 
                    'content': generate_prompt
                },
            ]
        )
        return response.choices[0].message.content
    
    def generate_FIBQs(self, title, num_of_fibqs,context, task):
        generate_prompt = f"""
            You are an expert, a very outstanding professor in Computer Science.
            I need you help me in domain of {title}. 
            Use your knowledge to generate to me {num_of_fibqs} fill in the blank questions relate to {task}.
            Here is a context that support you to generate fill in the blank questions: 
            ------------------------------
            {context}
            ------------------------------
            . Note that if context is empty or not support enough information, you must use
            specific-domain knowledge to back up.
            . You must follow the pattern here:
                - Start each question number with 1., 2., etc.
                - Start the corrected answer with pattern 'The correct answer is: '. (Note: If it has multiple-answer, must use '/' only, don't show more)
                - Start the explanation by 'Explanation:', you should explain why it is correct.
                - Start the reference by 'For more information:', you refer useful link relate to Computer Science
                as you know (GeeksForGeeks, Wikipedia, etc).
        """
        response = self.__llm.chat.complete(
            model=model2,
            messages=[
                {
                    'role': 'user', 
                    'content': generate_prompt
                },
            ]
        )
        return response.choices[0].message.content
    
    