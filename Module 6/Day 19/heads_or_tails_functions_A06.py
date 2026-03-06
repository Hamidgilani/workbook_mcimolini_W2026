import random

# Function definitions (defs) should be at the top of your file
def get_user_guess():
    user_guess = input("Guess the coin flip! Enter heads or tails (h/t): ")
    return user_guess

# This function returs a value. I can do this through multiple returns, or a returned variable
def get_coin_flip():
    random_number = random.randint(0, 1)
    
    if random_number == 0:
        print("The coin flip was: heads")
        return "h"
    else:
        print("The coin flip was: tails")
        return "t"

# This function takes 2 parameters and returns nothing.
def game_play(flip, guess):
        if ((flip == 0 and guess == "h")
        or (flip == 1 and guess == "t")):
            print("you guessed correct!")
        else:
            print("you guessed wrong!")

if __name__ == "__main__":
    user_guess = get_user_guess()

    random_flip = get_coin_flip()

    game_play(random_flip, user_guess)