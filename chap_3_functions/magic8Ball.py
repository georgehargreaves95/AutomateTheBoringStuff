# A functional fortune teller

import random


def get_answers(answer_number):
    if answer_number == 0:
        return "It is certain"
    elif answer_number == 1:
        return "I cannot be sure"
    else:
        return "Ask again later"


fortune = random.randint(0, 3)
print(str(fortune) + " " + get_answers(fortune))
