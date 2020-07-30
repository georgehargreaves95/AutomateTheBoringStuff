# Defining some passing references

def eggs(some_param):
    some_param.append("Hello")


spam = [1, 2, 3]
eggs(spam)
print(spam)

