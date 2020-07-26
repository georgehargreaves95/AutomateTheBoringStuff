# Collatz function practice project


def collatz(number):  # Generates a Collatz sequence from the argument
    if number % 2 == 0:
        result = number // 2
    else:
        result = (number * 3) + 1
    print(result)
    return result


def __main__():
    if __name__ == '__main__':
        try:  # Catches any attempt to use invalid values.
            starter = int(input("Enter a number:"))
            while starter != 1:  # Iterates until Collatz is complete (result is returned as 1
                starter = collatz(starter)
        except ValueError:
            print("Invalid argument, you must enter an int!")
            __main__()  # Restarts the programme on an invalid argument


__main__()
