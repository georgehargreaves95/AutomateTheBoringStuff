# This program demonstrates flow control, aka vampire

name = "Carol"
age = 3000
names = ["Alice", "Mary", "Frank", "James", "Mark", "Carol"]
ages = [10, 58, 42, 101, 50, 3000]


def vampire1(): # Working if/else tree
    if name == "Alice":
        print("Hi, Alice")
    elif age < 12:
        print("You're not Alice, young'un")
    elif age > 2000:
        print("Wait...I know what you are!!")
        print(".")
        print(".")
        print("Don't come any closer!")
        print(".")
        print("*screaming*")
    elif age > 100:
        print("Go back to bed, Grandma")
    return


def vampire2(): # Has a deliberate bug that won't ever print the vampire text
    if name == "Alice":
        print("Hi, Alice")
    elif age < 12:
        print("You're not Alice, young'un")
    elif age > 100:
        print("Go back to bed, old timer")
    elif age > 2000:
        print("Wait...I know what you are!!")
        print(".")
        print(".")
        print("Don't come any closer!")
        print(".")
        print("*screaming*")
    return


def vampire3():  # While loop which displays all linear outcomes from two lists
    i = 0
    while i < 6:
        loop_name = names[i]
        loop_age = ages[i]
        if loop_name == "Alice":
            print("Hi, Alice")
        elif loop_name == "Mark":
            print("Oh hi Mark")
        else:
            print("You're not Alice, you're " + loop_name)

        if loop_age < 12:
            print("Run along, young'un")
        elif loop_age > 2000:
            print("Wait...I know what you are!!")
            print(".")
            print(".")
            print("Don't come any closer!")
            print(".")
            print("*screaming*")
        elif loop_age > 100:
            print("Go back to bed, old timer")
        else:
            print("There's something wicked about, best get home!")
        i += 1
        print()
    return

