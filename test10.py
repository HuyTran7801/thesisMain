from model.MultiAgentDebate import *
from model.Handling import *

fibqs = f"""
1. Encapsulation helps achieve _______ _______.
    The correct answer is: data hiding, data abstraction/abstraction
    Explanation:  Encapsulation hides internal data representation and implementation details from the outside world.
    For more information: https://www.geeksforgeeks.org/encapsulation-in-java/


2. The "is-a" relationship is commonly used to describe _______.
    The correct answer is: `inheritance`
    Explanation: If class B inherits from class A, we say that B "is a" type of A.
    For more information: https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)

3. _______ is a form of inheritance where a class inherits from multiple superclasses. While Java doesn't directly support this with classes, it achieves a similar result through _______.
    The correct answer is: Multiple inheritance, interfaces
    Explanation: Multiple inheritance allows a class to inherit from more than one parent class, but Java uses interfaces to provide some of the benefits of multiple inheritance.
    For more information: https://en.wikipedia.org/wiki/Multiple_inheritance

4. To create a read-only member in Java, you can use the _______ access modifier and provide a _______ but not a _______ method.
    The correct answer is: private, getter, setter
    Explanation: This allows external access to the value but prevents modification.
    For more information: https://www.geeksforgeeks.org/getter-and-setter-methods-in-java/

5. In inheritance, a subclass can _______ methods inherited from its superclass to provide specialized behavior.
    The correct answer is: override
    Explanation: Overriding allows a subclass to provide a specific implementation for a method that is already defined in its superclass.
    For more information: https://www.geeksforgeeks.org/overriding-in-java/
"""
multi_agent = MultiAgent()

multi_agent.generate_FIBQs('Object-oriented Programming', 10, '', 'Inheritance and Encapsulation')

print('___ANS___')
ans = multi_agent.get_FIBQs()
print(ans)
print('---------')
handling = Handling()

fibqs_lst = handling.split_5_mcqs(ans)
# print(len(fibqs_lst))
# print(fibqs_lst)
# print('______')

for i in fibqs_lst:
    question, feedback_lst, corrected_answer = handling.split_QA_fill_in_the_blank(i)
    # print('Question: ', question)
    # print('Feedback')
    # print(feedback_lst)
    print('-------')
    print('Corrected ans ')
    if ',' in corrected_answer:
        corrected_answer = corrected_answer.split(",")
        for j in range(len(corrected_answer)):
            if '/' in corrected_answer[j]:
                corrected_answer[j] = corrected_answer[j].split('/')
        for j in range(len(corrected_answer)):
            if isinstance(corrected_answer[j], list) == True:
                for k in range(len(corrected_answer[j])):
                    corrected_answer[j][k] = corrected_answer[j][k].replace('`', '').strip()
            else:
                corrected_answer[j] = corrected_answer[j].replace('`', '').strip()
    else:
        if '/' in corrected_answer:
            corrected_answer = corrected_answer.split('/')
            for j in range(len(corrected_answer)):
                corrected_answer[j] = corrected_answer[j].replace('`','').strip()
        else:
            # None
            corrected_answer = corrected_answer.replace('`','').strip()
    print(corrected_answer)
    print('____')