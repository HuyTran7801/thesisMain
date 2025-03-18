from model.Handling import *
from model.MultiAgentDebate import *

# multi_agent = MultiAgent()
# multi_agent.generate_MCQs('Probability', 10, '', 'basic of probability')
mcqs10 ="""
I.  A bag contains 3 red balls and 5 blue balls. One ball is drawn at random. What is the probability that the ball drawn is blue?
A) 3/8
B) 5/8
C) 3/5
D) 5/3
The correct answer is: B)
Explanation: There are a total of 3 + 5 = 8 balls.  5 of them are blue. Therefore, the probability of drawing a blue ball is 5/8.
For more information: https://www.mathsisfun.com/data/probability-events-certain.html


II.  Two fair coins are tossed. What is the probability of getting at least one head?
A) 1/4
B) 1/2
C) 3/4
D) 1
The correct answer is: C)
Explanation: The possible outcomes are HH, HT, TH, TT.  Three of these have at least one head. So the probability is 3/4.
For more information: https://www.geeksforgeeks.org/probability-of-getting-at-least-k-heads-in-n-coin-tosses/

III. A six-sided die is rolled. What is the probability of rolling an even number?
A) 1/6
B) 1/3
C) 1/2
D) 2/3
The correct answer is: C)
Explanation: The even numbers are 2, 4, and 6. There are 3 even numbers out of 6 possible outcomes. The probability is 3/6 = 1/2.
For more information:  https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/v/probability-with-dice

IV.  If the probability of an event A is 0.6, what is the probability of the complement of A (A not happening)?
A) 0.4
B) 0.6
C) 1
D) 0
The correct answer is: A)
Explanation: The complement of an event is 1 minus the probability of the event.  So, 1 - 0.6 = 0.4.
For more information: https://en.wikipedia.org/wiki/Complementary_event


V. Events A and B are independent. P(A) = 0.2 and P(B) = 0.3. What is the probability of both A and B occurring? (Remember, independent events mean the outcome of one doesn't affect the other.)
A) 0.5
B) 0.06
C) 0.6
D) 0.1
The correct answer is: B)
Explanation: For independent events, the probability of both occurring is the product of their individual probabilities: P(A and B) = P(A) * P(B) = 0.2 * 0.3 = 0.06.        
For more information: https://www.probabilitycourse.com/chapter1/1_4_4_independent_events.php

VI. A card is drawn from a standard deck of 52 cards. What is the probability that the card is a heart?
A) 1/52
B) 1/13
C) 1/4
D) 4/13
The correct answer is: C)
Explanation: There are 13 hearts in a deck of 52 cards.  The probability of drawing a heart is 13/52 = 1/4.
For more information:  https://www.khanacademy.org/math/statistics-probability/counting-permutations-and-combinations

VII.  A spinner has 8 equal sections numbered 1 through 8. What is the probability of the spinner landing on a number greater than 5?
A) 1/8
B) 3/8
C) 5/8
D) 1/2
The correct answer is: B)
Explanation: The numbers greater than 5 are 6, 7, and 8.  There are 3 such outcomes. The probability is 3/8.
For more information: https://www.mathsisfun.com/data/spinner.html

VIII. A coin is flipped and a six-sided die is rolled. What is the probability of getting heads and rolling a number less than 3?
A) 1/12
B) 1/6
C) 1/4
D) 1/3
The correct answer is: A)
Explanation: The probability of getting heads is 1/2.  The numbers less than 3 are 1 and 2, so the probability of rolling less than 3 is 2/6 = 1/3.  The probability of both events is (1/2) * (1/3) = 1/6.  This answer was corrected for accuracy.
For more information: https://www.ck12.org/probability/independent-events/lesson/Independent-Events-ALG-II/

IX. You roll a fair six-sided die twice. What is the probability of rolling a 2 on the first roll and an odd number on the second roll?
A) 1/12
B) 1/6
C) 1/4
D) 1/36
The correct answer is: A)
Explanation: The probability of rolling a 2 is 1/6. The probability of rolling an odd number (1, 3, or 5) is 3/6 = 1/2. The probability of both events is (1/6) * (1/2) = 1/12.
For more information: https://www.mathsisfun.com/data/probability-events-independent.html


X. A bag contains 2 red marbles and 4 blue marbles.  You draw one marble, put it back in the bag, and then draw another marble. What is the probability that both marbles drawn are red?
A) 1/9
B) 1/6
C) 1/3
D) 2/9
The correct answer is: A)
Explanation: The probability of drawing a red marble is 2/6 = 1/3. Since you replace the marble, the second draw has the same probability. The probability of drawing two red marbles is (1/3) * (1/3) = 1/9.
For more information: https://www.mathsisfun.com/data/probability-events-independent.html
"""

mcqs5 = """

I.  A bag contains 3 red balls and 5 blue balls. One ball is drawn at random. What is the probability that the ball drawn is blue?
A) 3/8
B) 5/8
C) 3/5
D) 5/3
The correct answer is: B)
Explanation: There are a total of 3 + 5 = 8 balls.  5 of them are blue. Therefore, the probability of drawing a blue ball is 5/8.
For more information: https://www.mathsisfun.com/data/probability-events-certain.html


II.  Two fair coins are tossed. What is the probability of getting at least one head?
A) 1/4
B) 1/2
C) 3/4
D) 1
The correct answer is: C)
Explanation: The possible outcomes are HH, HT, TH, TT.  Three of these have at least one head. So the probability is 3/4.
For more information: https://www.geeksforgeeks.org/probability-of-getting-at-least-k-heads-in-n-coin-tosses/

III. A six-sided die is rolled. What is the probability of rolling an even number?
A) 1/6
B) 1/3
C) 1/2
D) 2/3
The correct answer is: C)
Explanation: The even numbers are 2, 4, and 6. There are 3 even numbers out of 6 possible outcomes. The probability is 3/6 = 1/2.
For more information:  https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/v/probability-with-dice

IV.  If the probability of an event A is 0.6, what is the probability of the complement of A (A not happening)?
A) 0.4
B) 0.6
C) 1
D) 0
The correct answer is: A)
Explanation: The complement of an event is 1 minus the probability of the event.  So, 1 - 0.6 = 0.4.
For more information: https://en.wikipedia.org/wiki/Complementary_event


V. Events A and B are independent. P(A) = 0.2 and P(B) = 0.3. What is the probability of both A and B occurring? (Remember, independent events mean the outcome of one doesn't affect the other.)
A) 0.5
B) 0.06
C) 0.6
D) 0.1
The correct answer is: B)
Explanation: For independent events, the probability of both occurring is the product of their individual probabilities: P(A and B) = P(A) * P(B) = 0.2 * 0.3 = 0.06.        
For more information: https://www.probabilitycourse.com/chapter1/1_4_4_independent_events.php
"""

mcqs15 = """

I.  A bag contains 3 red balls and 5 blue balls. One ball is drawn at random. What is the probability that the ball drawn is blue?
A) 3/8
B) 5/8
C) 3/5
D) 5/3
The correct answer is: B)
Explanation: There are a total of 3 + 5 = 8 balls.  5 of them are blue. Therefore, the probability of drawing a blue ball is 5/8.
For more information: https://www.mathsisfun.com/data/probability-events-certain.html


II.  Two fair coins are tossed. What is the probability of getting at least one head?
A) 1/4
B) 1/2
C) 3/4
D) 1
The correct answer is: C)
Explanation: The possible outcomes are HH, HT, TH, TT.  Three of these have at least one head. So the probability is 3/4.
For more information: https://www.geeksforgeeks.org/probability-of-getting-at-least-k-heads-in-n-coin-tosses/

III. A six-sided die is rolled. What is the probability of rolling an even number?
A) 1/6
B) 1/3
C) 1/2
D) 2/3
The correct answer is: C)
Explanation: The even numbers are 2, 4, and 6. There are 3 even numbers out of 6 possible outcomes. The probability is 3/6 = 1/2.
For more information:  https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/v/probability-with-dice

IV.  If the probability of an event A is 0.6, what is the probability of the complement of A (A not happening)?
A) 0.4
B) 0.6
C) 1
D) 0
The correct answer is: A)
Explanation: The complement of an event is 1 minus the probability of the event.  So, 1 - 0.6 = 0.4.
For more information: https://en.wikipedia.org/wiki/Complementary_event


V. Events A and B are independent. P(A) = 0.2 and P(B) = 0.3. What is the probability of both A and B occurring? (Remember, independent events mean the outcome of one doesn't affect the other.)
A) 0.5
B) 0.06
C) 0.6
D) 0.1
The correct answer is: B)
Explanation: For independent events, the probability of both occurring is the product of their individual probabilities: P(A and B) = P(A) * P(B) = 0.2 * 0.3 = 0.06.        
For more information: https://www.probabilitycourse.com/chapter1/1_4_4_independent_events.php

VI. A card is drawn from a standard deck of 52 cards. What is the probability that the card is a heart?
A) 1/52
B) 1/13
C) 1/4
D) 4/13
The correct answer is: C)
Explanation: There are 13 hearts in a deck of 52 cards.  The probability of drawing a heart is 13/52 = 1/4.
For more information:  https://www.khanacademy.org/math/statistics-probability/counting-permutations-and-combinations

VII.  A spinner has 8 equal sections numbered 1 through 8. What is the probability of the spinner landing on a number greater than 5?
A) 1/8
B) 3/8
C) 5/8
D) 1/2
The correct answer is: B)
Explanation: The numbers greater than 5 are 6, 7, and 8.  There are 3 such outcomes. The probability is 3/8.
For more information: https://www.mathsisfun.com/data/spinner.html

VIII. A coin is flipped and a six-sided die is rolled. What is the probability of getting heads and rolling a number less than 3?
A) 1/12
B) 1/6
C) 1/4
D) 1/3
The correct answer is: A)
Explanation: The probability of getting heads is 1/2.  The numbers less than 3 are 1 and 2, so the probability of rolling less than 3 is 2/6 = 1/3.  The probability of both events is (1/2) * (1/3) = 1/6.  This answer was corrected for accuracy.
For more information: https://www.ck12.org/probability/independent-events/lesson/Independent-Events-ALG-II/

IX. You roll a fair six-sided die twice. What is the probability of rolling a 2 on the first roll and an odd number on the second roll?
A) 1/12
B) 1/6
C) 1/4
D) 1/36
The correct answer is: A)
Explanation: The probability of rolling a 2 is 1/6. The probability of rolling an odd number (1, 3, or 5) is 3/6 = 1/2. The probability of both events is (1/6) * (1/2) = 1/12.
For more information: https://www.mathsisfun.com/data/probability-events-independent.html


X. A bag contains 2 red marbles and 4 blue marbles.  You draw one marble, put it back in the bag, and then draw another marble. What is the probability that both marbles drawn are red?
A) 1/9
B) 1/6
C) 1/3
D) 2/9
The correct answer is: A)
Explanation: The probability of drawing a red marble is 2/6 = 1/3. Since you replace the marble, the second draw has the same probability. The probability of drawing two red marbles is (1/3) * (1/3) = 1/9.
For more information: https://www.mathsisfun.com/data/probability-events-independent.html


XI.  A bag contains 3 red balls and 5 blue balls. One ball is drawn at random. What is the probability that the ball drawn is blue?
A) 3/8
B) 5/8
C) 3/5
D) 5/3
The correct answer is: B)
Explanation: There are a total of 3 + 5 = 8 balls.  5 of them are blue. Therefore, the probability of drawing a blue ball is 5/8.
For more information: https://www.mathsisfun.com/data/probability-events-certain.html


XII.  Two fair coins are tossed. What is the probability of getting at least one head?
A) 1/4
B) 1/2
C) 3/4
D) 1
The correct answer is: C)
Explanation: The possible outcomes are HH, HT, TH, TT.  Three of these have at least one head. So the probability is 3/4.
For more information: https://www.geeksforgeeks.org/probability-of-getting-at-least-k-heads-in-n-coin-tosses/

XIII. A six-sided die is rolled. What is the probability of rolling an even number?
A) 1/6
B) 1/3
C) 1/2
D) 2/3
The correct answer is: C)
Explanation: The even numbers are 2, 4, and 6. There are 3 even numbers out of 6 possible outcomes. The probability is 3/6 = 1/2.
For more information:  https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/v/probability-with-dice

XIV.  If the probability of an event A is 0.6, what is the probability of the complement of A (A not happening)?
A) 0.4
B) 0.6
C) 1
D) 0
The correct answer is: A)
Explanation: The complement of an event is 1 minus the probability of the event.  So, 1 - 0.6 = 0.4.
For more information: https://en.wikipedia.org/wiki/Complementary_event


XV. Events A and B are independent. P(A) = 0.2 and P(B) = 0.3. What is the probability of both A and B occurring? (Remember, independent events mean the outcome of one doesn't affect the other.)
A) 0.5
B) 0.06
C) 0.6
D) 0.1
The correct answer is: B)
Explanation: For independent events, the probability of both occurring is the product of their individual probabilities: P(A and B) = P(A) * P(B) = 0.2 * 0.3 = 0.06.        
For more information: https://www.probabilitycourse.com/chapter1/1_4_4_independent_events.php
"""

handling = Handling()
print('LIST OF 10')
mcqs_lst10 = handling.split_10_mcqs(mcqs10)
# print('len ', len(mcqs_lst))
for i in range(len(mcqs_lst10)):
    print('QUESTION ', (i + 1))
    print(mcqs_lst10[i])
    print('___________')
    
print('LIST OF 5')
mcqs_lst5 = handling.split_5_mcqs(mcqs5)
for i in range(len(mcqs_lst5)):
    print('QUESTION ', (i + 1))
    print(mcqs_lst5[i])
    print('___________')
    
print('LIST OF 15')
mcqs_lst15 = handling.split_15_mcqs(mcqs15)
for i in range(len(mcqs_lst15)):
    print('QUESTION ', (i + 1))
    print(mcqs_lst15[i])
    print('___________')


# for i in mcqs_lst:
# question, answer_lst, feedback_lst, corrected_ans = handling.split_QA(mcqs_lst[0])
# print('Question ', question)
# print('Answer ')
# for j in answer_lst:
#     print(j)
# print('Feedback')
# for j in feedback_lst:
#     print(j)
# print('Corrected aans ', corrected_ans)