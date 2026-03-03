import random

# Functions definitions should be at the top of your file 
def get_user_guess():
    user_guess =  input("Guess the coin flip! Enter heads or tails (h/t): ")
    return user_guess
# heads will be 0 and tails will be 1
def get_coin_flip():
    random_number = random.randint(0, 1)
    if random_number == 0:
        print("The coin flip was: heads")
        return "h"
    else:
        print("The coin flip was: tails")
        return "t"

user_guess = get_user_guess()
def game_play(flip,guess):
    if random_number == 0:
        print("The coin flip was: heads")
    elif random_number == 1:
        print("The coin flip was: tails")

    if ((random_number == 0 and user_guess == "h")
        or (random_number == 1 and user_guess == "t")):
        print("you guessed correct!")
    else:
        print("you guessed wrong!")


if __name__ == "_main_":
    user_guess = get_user_guess()
    random_flip = get_coin_flip()
    game_play(random_flip, user_guess)