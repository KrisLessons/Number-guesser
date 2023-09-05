# number guessing game
# input the user for the difficulty of the game hard, medium and easy
# based on that hard = 100000, medium = 10000, easy = 10000
# generate a random number in that sequence
# let the user have 10 guesses about the number
# if the guess is lower than the random number (target) give him a hint that he must go upwards
# otherwise do the opposite thing
# if the user wins. Show him how many tries it took him to win

import random


# loops == recursion
# idiomatic -> the standard way to do things
def get_difficulty():
    # while loop is used to reprompt the user on idiotic behavior
    while True:
        difficulty = input(
            "Choose a difficulty level (E)asy, (M)edium, (H)ard): "
        ).lower()

        if difficulty.startswith("h"):
            return 10000
        elif difficulty.startswith("m"):
            return 1000
        elif difficulty.startswith("e"):
            return 100
        else:
            continue


def get_difficulty_two():
    difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
    match difficulty:
        case "hard":
            return 10000
        case "medium":
            return 1000
        case "easy":
            return 100
        case _:
            print("Invalid difficulty level. Please choose easy, medium, or hard.")
            return (
                get_difficulty_two()
            )  # recursion (call the same function from inside) is used to reprompt the user


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# input -> output
# input = "eas"
# desired output -> reprompt the user
# current output -> end of program
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def play_game():
    print("Welcome to the number guessing game!")

    range_limit = get_difficulty()

    target = random.randint(1, range_limit)
    attempts = 0

    print(f"Guess the number between 1 and {range_limit}")

    while attempts < 10:
        guess = input("Enter your guess here: ")

        if not guess.isdigit():
            print("Please enter a valid number, then try again!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < target:
            print("Try higher!")
        elif guess > target:
            print("Try lower!")
        else:
            print(
                f"Congratulations! You guessed the number {target} correctly in {attempts} attempts."
            )
            return

    print("Sorry, you didn't gueesed the number in the 10 atempts set by the game.")
    print(f"The correct number was {target}. Good luck next time!")


# is this python file envoked from here or is it imported?
if __name__ == "__main__":
    play_game()
