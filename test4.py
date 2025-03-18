from model.MultiAgentDebate import *


multi_agent = MultiAgent()

multi_agent.generate_hard_MCQs('Data structure and Algorithm', 15, '', 'graph theory')
ans = multi_agent.get_MCQs()

print('FINAL ANS')
print(ans)