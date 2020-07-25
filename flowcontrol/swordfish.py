# While statement demo
import sys


def demo1():
    while True:
        print("Who are you?")
        name = input()
        if name != "Joe":
            continue
        print("Hello, Joe. What's the password?")
        password = input()
        if password == "swordfish":
            break
    print("Access granted.")


def demo2():
    while True:
        print("Type `exit` to exit")
        response = input()
        if response == "exit":
            sys.exit()
        print("You typed: " + response)


def __main__():
    if __name__ == '__main__':
        print("Welcome to swordfish!")
        demo1()
        demo2()


__main__()
