from model.MultiAgentDebate import *
from time import *

mcqs="""
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


**1.** You are designing a logging system for a complex application.  You want to allow clients to easily switch between different logging implementations (e.g., file-based, database-based, console-based) without modifying the core application logic.  Which pattern is the most appropriate?

A) Abstract Factory
B) Strategy
C) Observer
D) Template Method

The correct answer is: B)
Explanation: The Strategy pattern encapsulates different algorithms (in this case, logging methods) and makes them interchangeable. Clients can select the desired logging strategy at runtime.
For more information: https://refactoring.guru/design-patterns/strategy

**2.** You're building an e-commerce platform and want to implement a flexible discount system.  Discounts can be based on various factors (e.g., quantity, customer loyalty, special promotions).  You want to be able to combine multiple discounts without modifying the core pricing logic. Which pattern best addresses this scenario?

A) Decorator
B) Composite
C) Chain of Responsibility
D) Visitor

The correct answer is: C)
Explanation: The Chain of Responsibility pattern allows you to pass requests along a chain of handlers. Each handler can decide whether to process the request (apply a discount) or pass it to the next handler. This enables flexible combination of discounts.
For more information: https://refactoring.guru/design-patterns/chain-of-responsibility

**3.** You need to create an object that represents a complex document structure with various elements (paragraphs, tables, images).  The structure should be easily traversable and allow operations on individual elements or the entire structure.  Which pattern is the most suitable?

A) Flyweight
B) Composite
C) Iterator
D) Proxy

The correct answer is: B)
Explanation:  The Composite pattern composes objects into tree structures to represent part-whole hierarchies. This allows clients to treat individual objects and compositions of objects uniformly, making it ideal for representing complex document structures.
For more information: https://refactoring.guru/design-patterns/composite


**4.** You are working on a game and want to implement different character types (e.g., warrior, mage, rogue). Each character type has unique abilities and behaviors.  You want to avoid creating large, complex class hierarchies. Which pattern is most effective in this situation?

A) Prototype
B) State
C) Template Method
D) Bridge

The correct answer is: D)
Explanation: The Bridge pattern decouples an abstraction from its implementation so that the two can vary independently.  This allows you to define character types (abstraction) separately from their abilities and behaviors (implementation), preventing class explosion.
For more information: https://refactoring.guru/design-patterns/bridge

**5.**  You have an existing class library, and you need to integrate it with a newer system that uses a different interface.  You want to minimize changes to both systems.  Which pattern is the most appropriate?

A) Facade
B) Decorator
C) Adapter
D) Proxy

The correct answer is: C)
Explanation: The Adapter pattern converts the interface of a class into another interface clients expect. This allows classes with incompatible interfaces to work together without modification.
For more information: https://refactoring.guru/design-patterns/adapter


**6.**  You're developing a text editor, and you want to implement undo/redo functionality. Which pattern is best suited for managing the history of operations?

A) Command
B) Memento
C) Interpreter
D) Iterator

The correct answer is: B)
Explanation: The Memento pattern captures and externalizes an object's internal state without violating encapsulation. This allows you to restore the object to a previous state, which is essential for undo/redo functionality.
For more information: https://refactoring.guru/design-patterns/memento

**7.**  You have a system with computationally expensive object creation.  You want to avoid creating new objects whenever possible and reuse existing instances if they have the same state.  Which pattern is the most suitable?

A) Singleton
B) Builder
C) Prototype
D) Flyweight

The correct answer is: C)
Explanation: The Prototype pattern creates new objects by copying existing instances (prototypes). This can be more efficient than creating objects from scratch, especially for complex objects.
For more information: https://refactoring.guru/design-patterns/prototype

**8.** You want to create a complex object with many optional parameters.  You want a flexible and readable way to construct this object step-by-step. Which pattern is most applicable?

A) Factory Method
B) Abstract Factory
C) Builder
D) Singleton

The correct answer is: C)
Explanation: The Builder pattern separates the construction of a complex object from its representation, allowing you to build different representations using the same construction process.  It's ideal for objects with numerous optional parameters.
For more information: https://refactoring.guru/design-patterns/builder

**9.** You need to implement an expression evaluator for a domain-specific language. Which pattern helps represent the grammar of the language and interpret expressions?    

A) Visitor
B) Interpreter
C) Command
D) Mediator

The correct answer is: B)
Explanation: The Interpreter pattern defines a representation for a grammar of a given language, along with an interpreter that uses the representation to interpret sentences in the language.  It's perfect for implementing expression evaluators and domain-specific languages.
For more information: https://refactoring.guru/design-patterns/interpreter

**10.** You're building a multi-threaded application and need to ensure that only one thread can access a shared resource at a time.  You want to avoid explicit locking mechanisms in your business logic. Which pattern is most suitable for managing concurrent access?

A) Proxy
B) Decorator
C) Flyweight
D) Monitor Object

The correct answer is: A)
Explanation: While not a traditional Gang of Four pattern, the Monitor Object pattern encapsulates the locking mechanism within a dedicated object (the monitor), simplifying concurrent access control and keeping it separate from the core logic.  A Proxy can act as a Monitor Object. This is a more advanced application of the Proxy pattern.      
For more information: https://en.wikipedia.org/wiki/Monitor_(synchronization)

**1.** You are designing a system where multiple algorithms can be applied to a dataset dynamically. These algorithms can be chained together, and the order of execution can be changed at runtime.  However, some algorithms are computationally expensive, and redundant calculations should be avoided. Which combination of patterns best addresses this requirement while considering performance?

A) Strategy and Decorator
B) Chain of Responsibility and Composite
C) Strategy and Chain of Responsibility with memoization
D) Template Method and Iterator

The correct answer is: C)
Explanation: Strategy allows interchangeable algorithms, and Chain of Responsibility enables their dynamic chaining and ordering. Incorporating memoization within the Chain of Responsibility can prevent redundant calculations and improve performance.
For more information: https://refactoring.guru/design-patterns/strategy and https://refactoring.guru/design-patterns/chain-of-responsibility


**2.** You are building a real-time stock trading application. You need to notify multiple components (e.g., trading bot, UI, logging system) about price changes. Performance is critical, but you also need to ensure reliable delivery of notifications. Which pattern offers the best balance of performance and reliability?

A) Observer using a push model with a dedicated message queue
B) Observer using a pull model
C) Reactor pattern
D) Mediator pattern

The correct answer is: A)
Explanation: While the Reactor pattern offers excellent performance, a push-based Observer with a message queue ensures reliable delivery even if some components are temporarily unavailable. The message queue acts as a buffer, preventing message loss.
For more information: https://en.wikipedia.org/wiki/Reactor_pattern and https://refactoring.guru/design-patterns/observer


**3.** You are designing an image processing application where users can select different filters (blur, sharpen, emboss, etc.) dynamically at runtime.  You want to minimize code duplication and make it easy to add new filters in the future. Which pattern is most suitable for implementing this filter selection feature?

A) Strategy
B) Abstract Factory
C) Command
D) Template Method


The correct answer is: A)
Explanation: The Strategy pattern allows you to encapsulate each filter as a separate algorithm, making them interchangeable and easy to add or remove without modifying the core application logic.
For more information: https://refactoring.guru/design-patterns/strategy

**4.** You are developing a caching system for frequently accessed data. You want to use multiple caching strategies (e.g., in-memory, distributed cache, file-based cache) and switch between them based on factors like data volatility and access frequency.  Each caching strategy has different performance characteristics and resource requirements.  Which pattern provides the most flexible and efficient solution considering these trade-offs?

A) Chain of Responsibility
B) Abstract Factory
C) Strategy
D) Bridge


The correct answer is: C)
Explanation: The Strategy pattern allows you to define a family of caching algorithms (strategies), encapsulate each one, and make them interchangeable at runtime. This gives you the flexibility to choose the optimal caching strategy based on various factors.
For more information: https://refactoring.guru/design-patterns/strategy

**5.** In a complex enterprise application, you need to track changes to business objects and provide auditing capabilities.  You want a mechanism to capture and restore the state of these objects at different points in time without exposing their internal structure. You also want to ensure that the history of changes is preserved even if the application crashes.  Which combination of patterns is most suitable, considering fault tolerance?

A) Memento and Command with persistent storage of mementos.
B) Command and Observer
C) Memento and Iterator
D) State and Strategy

The correct answer is: A)
Explanation: Memento captures object state, and Command encapsulates state-modifying operations.  Storing mementos persistently (e.g., in a database) provides fault tolerance by ensuring that the change history is not lost in case of application failure.
For more information: https://refactoring.guru/design-patterns/memento and https://refactoring.guru/design-patterns/command

**6.** You're working with a legacy system with complex and poorly documented APIs. You want to simplify interaction with this system for new client applications without modifying the legacy code. You also want to log all interactions with the legacy system for debugging and monitoring purposes. Which pattern is the best choice, considering this additional logging requirement?

A) Decorator
B) Adapter with a logging decorator
C) Facade with integrated logging
D) Proxy

The correct answer is: C)
Explanation: A Facade provides a simplified interface to the legacy system. Integrating logging directly into the Facade centralizes this functionality and ensures consistent logging for all client interactions.
For more information: https://refactoring.guru/design-patterns/facade

**7.** You need to create a system that can handle a large number of objects efficiently, many of which share common properties. You want to minimize memory usage by sharing these common properties, but you also need to allow for some objects to have unique variations. Which pattern is specifically designed for this scenario?

A) Prototype
B) Flyweight
C) Singleton
D) Composite

The correct answer is: B)
Explanation: Flyweight excels at minimizing memory usage by sharing intrinsic state (common properties) among multiple objects.  It can also accommodate variations by allowing objects to store extrinsic state (unique properties) separately.
For more information: https://refactoring.guru/design-patterns/flyweight

**8.** You want to create a system where complex objects can be cloned easily, allowing for variations and customizations without modifying the original object. However, some objects have circular references or contain large amounts of data, which can make deep cloning costly. Which pattern facilitates this requirement while minimizing the potential performance overhead of cloning?

A) Builder
B) Prototype with shallow copy and copy-on-write for mutable objects
C) Factory Method
D) Abstract Factory

The correct answer is: B)
Explanation:  The Prototype pattern allows for cloning.  Using shallow copy and copy-on-write optimizations reduces the initial overhead of cloning, particularly with large or complex objects, delaying deep copying until necessary.


For more information: https://refactoring.guru/design-patterns/prototype

**9.** You're developing a game where the behavior of a character changes based on its internal state (e.g., healthy, injured, poisoned). Each state transition can have complex side effects (e.g., applying visual effects, triggering sound effects). Which pattern is most suitable for managing these state-dependent behaviors and associated side effects?

A) Strategy
B) State
C) Template Method
D) Chain of Responsibility


The correct answer is: B)
Explanation: The State pattern encapsulates state-specific behavior and handles state transitions gracefully. This makes it easy to manage complex side effects associated with each state change by encapsulating them within the respective state classes.
For more information: https://refactoring.guru/design-patterns/state

**10.**  You are building a graphical editor with various shapes (circles, rectangles, triangles). You want to define operations that can be performed on these shapes (e.g., move, resize, rotate) without modifying the shape classes themselves. You also want to avoid creating dependencies between the operation logic and the concrete shape classes. Which pattern is the most appropriate?


A) Interpreter
B) Mediator
C) Visitor
D) Command

The correct answer is: C)
Explanation:  The Visitor pattern lets you define new operations without altering existing shape classes.  Crucially, it avoids creating strong dependencies between operations and concrete shapes, promoting better separation of concerns and extensibility.
For more information: https://refactoring.guru/design-patterns/visitor
"""

multi_agent = MultiAgent()

multi_agent.generate_hard_MCQs(mcqs, 10, 'Design Pattern')

print('----HARD MCQs----')
mcqs2 = multi_agent.get_MCQs()
print(mcqs2)
print('-------------------------')


# sleep(10)

# multi_agent.generate_distractors(mcqs2, 10, 'Design Pattern')

# print('------HARD MCQs ROUND 2------')
# print(multi_agent.get_MCQs())
# print('-----------------------------')