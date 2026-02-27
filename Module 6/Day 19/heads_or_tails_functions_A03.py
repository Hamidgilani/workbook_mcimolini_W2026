import random

# Functions need to be defined before they are used.
# Conventionally this will be at the top of your file.

# We can return a single variable or have multiple return paths
def get_coin_flip():
    random_number = random.randint(0, 1)

    if random_number == 0:
        print("The coin flip was: heads")
        return "h"
    else:
        print("The coin flip was: tails")
        return "t"

def get_user_guess():
    user_guess = input("Guess the coin flip! Enter heads or tails (h/t): ")
    return user_guess

if __name__ == "__main__":
    user_guess = get_user_guess()

    random_flip = get_coin_flip()

    if ((random_flip == 0 and user_guess == "h")
        or (random_flip == 1 and user_guess == "t")):
        print("you guessed correct!")
    else:
        print("you guessed wrong!")
