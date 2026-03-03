import random 

from rps_functions import convert_input_to_result
from rps_functions import check_result

if __name__ == "__main__":
    user_input = int(input("Scissor(0), rock(1), paper(2): "))
    computer_input = random.randint(0,2)

    user_result = convert_input_to_result(user_input)
    computer_result = convert_input_to_result(computer_input)

    check_result = (user_result,computer_result)


