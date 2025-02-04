
class MCQs:
    def __init__(self, domain, question, answer, fail_attempt):
        self.__domain = domain
        self.__question = question
        self.__answer= answer
        self.__fail_attempt = fail_attempt
        
    def get_domain(self):
        return self.__domain

    def set_domain(self, domain):
        self.__domain = domain
    
    def get_question(self):
        return self.__question

    def set_question(self, question):
        self.__question = question
    
    def get_answer(self):
        return self.__answer
    
    def set_answer(self, answer):
        self.__answer = answer
    
    def get_fail_attempt(self):
        return self.__fail_attempt        
    
    def set_fail_attempt(self, fail_attempt):
        self.__fail_attempt = fail_attempt