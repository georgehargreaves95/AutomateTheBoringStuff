# A brief discussion on variable scopes


def local_global_same_name():
    eggs = "eggs local"
    print(eggs)  # prints eggs local


def more_local_less_global():
    eggs = "bacon local"
    print(eggs)
    local_global_same_name()
    print(eggs)


eggs = "global"
more_local_less_global()
print(eggs)


def global_statement_demo():
    global eggs
    eggs = "spam"


eggs = "global"
global_statement_demo()
print(eggs)


def global_statement_demo_2():
    eggs = "bacon"


def global_statement_demo_3():
    print("eggs")


eggs = 42
global_statement_demo()
print(eggs)

