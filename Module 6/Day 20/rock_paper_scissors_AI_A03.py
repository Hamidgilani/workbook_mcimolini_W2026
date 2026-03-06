import random

# We can reuse our "library" in other programs

from rps_functions_A03 import translate_choice, get_game_result

if __name__ == "__main__":
    while True:

        p1_result = translate_choice(random.randint(0, 2))
        p2_result = translate_choice(random.randint(0, 2))

        get_game_result(p1_result, p2_result)

        play_again = input("Play again? (Y/N) ").upper()

        if(play_again == "N"):
            print("Thanks for playing!")            
            break