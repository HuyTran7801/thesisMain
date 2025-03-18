from model.MultiAgentDebate import *


multi_agent = MultiAgent()

mcqs = """
**VI.** You're working with a legacy system with complex and poorly documented APIs. You want to simplify interaction with this system for new client applications without modifying the legacy code. You also want to log all interactions with the legacy system for debugging and monitoring purposes. Which pattern is the best choice, considering this additional logging requirement?

A) Decorator
B) Adapter with a logging decorator
C) Facade with integrated logging
D) Proxy

The correct answer is: C)
Explanation: A Facade provides a simplified interface to the legacy system. Integrating logging directly into the Facade centralizes this functionality and ensures consistent logging for all client interactions.
For more information: https://refactoring.guru/design-patterns/facade

"""

multi_agent.generate_MCQs_human_in_the_loop('Object Oriented Programming',mcqs, 'I want it in a coding', 'Design Pattern')

ans = multi_agent.get_MCQs()

print('FINAL ANS')
print(ans)
print('_________')