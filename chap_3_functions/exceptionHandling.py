# Checking out some exception handling


def divide_42(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError:
        print("Invalid argument, can't divide by zero!")


def zero_divide():
    print(divide_42(2))
    print(divide_42(0))
    print(divide_42(12))


zero_divide()

