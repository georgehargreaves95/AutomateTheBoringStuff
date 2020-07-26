# Simple guess the number game

import random
import sys


def game() -> bool:
    secret_number = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20")
    win = False

    # Ask the player to guess 6 times
    for guessesTaken in range(1, 7):
        guess = int(input("Take a guess: "))

        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            break
    if guess == secret_number:
        print("Good Job! You guessed my number in " + str(guessesTaken) + " guesses")
        win = True
    else:
        print("Nope! The number I was thinking of is " + str(secret_number))

    return win


def __main__():
    if __name__ == '__main__':
        print("Welcome to the random number game!")
        lives = 3
        # Set up a loop that will allow replays
        while True:
            if not game():
                lives -= 1

            if lives == 0:
                print("You've run out of lives! Better luck next time")
                sys.exit()

            again = input("Wanna play again Y/N? ")
            if again == "Y":
                continue
            else:
                print("Bye!")
                sys.exit()


__main__()
