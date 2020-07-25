# This program says hello and asks for my name

print("Hello World")
print("What is your name?")  # Ask for user name
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is: ")
print(len(myName))
print("What is your age?")   # Ask for user age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " next year.")
