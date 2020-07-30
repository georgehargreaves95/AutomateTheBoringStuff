# Learning about copy

import copy

spam = ['A', 'B', 'C', 'D', 'E']
print("spam id: " + str(id(spam)))
cheese = copy.copy(spam)
print("cheese id: " + str(id(cheese)))
cheese[2] = 42
print(spam + cheese)
