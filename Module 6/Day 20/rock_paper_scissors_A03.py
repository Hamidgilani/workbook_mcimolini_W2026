# if your files are in different folders, you need a file named __init__.py inside the folder
# to get things to work. Also required in older version of python

import random

from rps_functions_A03 import translate_choice
from rps_functions_A03 import get_game_result

# could also do:
# from rps_functions_A03 import translate_coice, get_game_result

if __name__ == "__main__":
    user_input =  int(input("Scissor (0), rock (1), paper (2): "))
    computer_input = random.randint(0, 2)

    user_result = translate_choice(user_input)
    computer_result = translate_choice(computer_input)

    get_game_result(user_result, computer_result)