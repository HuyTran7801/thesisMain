from model.RAG import *
import os
from model.ReasoningLLM import *
from model.LLM import *
from model.Handling import *

handling = Handling()
rag = RAG('./data/oop/user1')
filename = 'OOP_Lesson03en.pdf'

docs = rag.load_documents('./static/files1')
# print(docs)
chunks = rag.split_documents(docs)
contexts = ''
for c in chunks:
    contexts += c.page_content
    
llm = ReasoningLLM('Object Oriented Programming', contexts, filename)
mcqs = llm.generate_MCQs_RAG()
print(mcqs)

text = f"""
1. Which of the following best describes data abstraction in the context of object-oriented programming?

A) Hiding complex implementation details and exposing only essential information to the user.
B) Using subprograms and control flow to manage program execution.
C) Defining specific instances of a concept or idea.
D) Grouping similar objects based on their physical characteristics.

The correct answer is: A)
Explanation: Data abstraction focuses on presenting only the necessary information about an object to the user, while hiding the underlying implementation. This simplifies interaction and promotes modularity.
For more information: Page 3, "Abstraction", OOP_Lesson03en.pdf.

2. What are the two main types of abstraction discussed in the context?

A) Data abstraction and process abstraction
B) Control abstraction and data abstraction
C) Class abstraction and object abstraction
D) Interface abstraction and implementation abstraction

The correct answer is: B)
Explanation: The lesson specifically mentions control abstraction (using subprograms and control flow) and data abstraction (e.g., data types).
For more information: Page 3, "Abstraction", OOP_Lesson03en.pdf.

3. In Java, how is an Abstract Data Type (ADT) typically implemented?

A) Using interfaces
B) Using abstract classes
C) Using classes
D) Using enums

The correct answer is: C)
Explanation: The text explicitly states, "Java allows implementing ADT in the form of classes."
For more information: Page 11, "Abstract data type", OOP_Lesson03en.pdf.

4.  What constitutes the signature of a method in Java?

A) The method's name and return type.
B) The method's name and the data types of its parameters.
C) The method's name, parameter names, and return type.
D) The method's access modifier, name, and parameter list.

The correct answer is: B)
Explanation:  The signature includes the method's name and the types of its parameters (in order), allowing the compiler to distinguish between overloaded methods.  The parameter *names* are not part of the signature.
For more information: Page 33-34 "Signature", OOP_Lesson03en.pdf.

5. Which keyword is used to declare a class variable in Java?

A) final
B) static
C) const
D) this

The correct answer is: B)
Explanation: The `static` keyword designates a variable as belonging to the class itself, rather than to any specific instance of the class.
For more information: Page 27, "Variable declaration", OOP_Lesson03en.pdf.

6. What is the purpose of access modifiers in Java?

A) To control the visibility and accessibility of class members.
B) To define the data type of variables.
C) To specify the inheritance hierarchy.
D) To manage memory allocation for objects.

The correct answer is: A)
Explanation: Access modifiers (public, private, protected, default) determine which parts of the code can access and modify class members.
For more information: Page 24, "Access modifier: Class’ and members’ visibility scope", OOP_Lesson03en.pdf.


7.  If a class member is declared without an access modifier, what is its visibility?

A) public
B) private
C) protected
D) package-private (default)

The correct answer is: D)
Explanation:  When no access modifier is specified, the member is accessible within the same package but not from outside the package. This is known as package-private or default access.
For more information: Page 24, "Access modifier: Class’ and members’ visibility scope", OOP_Lesson03en.pdf.

8.  What is the primary way objects interact with each other in object-oriented programming?

A) Direct memory access
B) Message passing
C) Shared variables
D) Static methods

The correct answer is: B)
Explanation: Objects communicate by sending messages to each other, invoking methods on the target object.
For more information: Page 16, "Message passing", OOP_Lesson03en.pdf.

9. Which of the following is NOT a benefit of using packages in Java?

A) Avoiding naming conflicts
B) Improving code readability
C) Increasing code execution speed
D) Controlling access to classes

The correct answer is: C)
Explanation: Packages primarily address organization and access control.  They do not directly impact execution speed.
For more information: Page 18, "Package", OOP_Lesson03en.pdf.

10. What is the relationship between a class and an object?

A) A class is an instance of an object.
B) An object is an instance of a class.
C) Classes and objects are unrelated concepts.
D) A class is a subclass of an object.

The correct answer is: B)
Explanation: A class is a blueprint or template, and an object is a concrete realization of that class.
For more information: Page 12, "Class", OOP_Lesson03en.pdf."""

