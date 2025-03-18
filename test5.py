from model.MultiAgentDebate import *
from model.RAG import *


# rag = RAG('./data/oop/user1')

# context, docs = rag.semantic_search('Design pattern', 8)

# multi_agent = MultiAgent()

# multi_agent.generate_MCQs('Object-oriented programming',10, context, 'Design Pattern')

# ans = multi_agent.get_MCQs()

# print('---ANS---')
# print(ans)

mcqs = """
You're absolutely right! My initial questions were too focused on definitions and lacked the depth needed to assess proper understanding.  I've taken your excellent feedback to heart and revised the questions to be more challenging and application-focused.

Here are the revised MCQs:

**1.** You are developing an application that needs to create different types of reports (PDF, CSV, HTML).  Which design pattern would be most suitable for creating these report objects without specifying their concrete classes?

A) Singleton
B) Observer
C) Factory Method
D) Adapter

The correct answer is: C)
Explanation: The Factory Method pattern provides an interface for creating objects, but lets subclasses decide which class to instantiate.  This is ideal for creating different report types based on a given input or condition.

For more information: https://refactoring.guru/design-patterns/factory-method

**2.**  Consider a scenario where you need to create families of related objects without specifying their concrete classes. Which pattern is most appropriate?

A) Factory Method
B) Abstract Factory
C) Builder
D) Prototype

The correct answer is: B)
Explanation: The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. This is different from Factory Method, which creates single objects.

For more information: https://refactoring.guru/design-patterns/abstract-factory


**3.** Which design pattern promotes loose coupling between objects by encapsulating the way objects interact?

A) Decorator
B) Mediator
C) Facade
D) Observer

The correct answer is: B)
Explanation: The Mediator pattern defines an object that encapsulates how a set of objects interact.  It promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.

For more information: https://refactoring.guru/design-patterns/mediator

**4.**  What is a key difference between the Adapter and Decorator patterns?

A) Adapter changes an interface, Decorator adds responsibilities.
B) Decorator changes an interface, Adapter adds responsibilities.
C) Both change the interface and add responsibilities.
D) Neither changes the interface nor adds responsibilities.

The correct answer is: A)
Explanation: The Adapter pattern converts the interface of a class into another interface clients expect, while the Decorator pattern adds responsibilities to an object dynamically.

For more information: https://stackoverflow.com/questions/57220/decorator-vs-adapter-pattern


**5.**  Which pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically?

A) Strategy
B) Observer
C) Singleton
D) Composite

The correct answer is: B)
Explanation:  The Observer pattern establishes a dependency between objects where one object (the subject) notifies its dependents (observers) of any state changes.

For more information: https://refactoring.guru/design-patterns/observer

**6.**  You have a class `Coffee` and want to add various condiments (milk, sugar, etc.) dynamically. Which pattern is most suitable?

A) Adapter
B) Facade
C) Decorator
D) Strategy

The correct answer is: C)
Explanation:  The Decorator pattern allows you to dynamically add responsibilities to an object by wrapping it in other objects, which is ideal for adding condiments to a coffee.

For more information: https://refactoring.guru/design-patterns/decorator

**7.** You want to ensure that a class has only one instance and provide a global point of access to it. Which pattern should you use?

A) Factory Method
B) Singleton
C) Prototype
D) Builder

The correct answer is: B)
Explanation: The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.

For more information: https://refactoring.guru/design-patterns/singleton

**8.** What's a potential drawback of the Singleton pattern?

A) Improved testability
B) Reduced global state
C) Difficulty in testing (due to global state)
D) Increased code complexity

The correct answer is: C)
Explanation: Singleton's global state can make unit testing difficult as it introduces dependencies that are hard to isolate.

For more information: https://softwareengineering.stackexchange.com/questions/40373/so-singletons-are-bad-then-what


**9.**  The code snippet below represents which creational design pattern?  (Assume `Product` is an interface and `ConcreteProductA`, `ConcreteProductB` are concrete classes implementing `Product`).

```java
interface Product {}
class ConcreteProductA implements Product {}
class ConcreteProductB implements Product {}

class Creator {
   public Product createProduct(String type) {
      if (type.equals("A")) {
         return new ConcreteProductA();
      } else if (type.equals("B")) {
         return new ConcreteProductB();
      }
       return null; // Or throw an exception
   }
}
```

A) Abstract Factory
B) Factory Method
C) Builder
D) Prototype

The correct answer is: B)
Explanation: The code demonstrates the Factory Method pattern.  The `Creator` class has a method that creates different product types based on an input parameter.

For more information:  https://www.geeksforgeeks.org/factory-method-design-pattern-in-java/


**10.** Which pattern provides a unified interface to a set of interfaces in a subsystem?

A) Adapter
B) Decorator
C) Facade
D) Proxy

The correct answer is: C)
Explanation: The Facade pattern provides a simplified interface to a complex subsystem, making it easier to use.

For more information: https://refactoring.guru/design-patterns/facade



These revised questions now focus more on application and understanding of core concepts, including trade-offs.  They cover a wider range of pattern categories and challenge students to think more critically about design patterns.
"""

multi_agent = MultiAgent()

multi_agent.retake_test(mcqs, 10, 'Design Pattern', '1, 9, 10')

print('-----RETAKE----')
print(multi_agent.get_MCQs())