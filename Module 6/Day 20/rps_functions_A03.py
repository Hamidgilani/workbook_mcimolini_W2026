# Could turn this into a single return by using a variable.
def translate_choice(number):
    #choice = ""
    if number == 0:
        return "scissor"
        #choice = "scissor"
    elif number == 1:
        return "rock"
        #choice = "rock"
    elif number == 2:
        return "paper"
        #choice = "paper"
    #return choice

def get_game_result(user_choice, computer_choice):
    #pass #pass is a keyword that lets us define a function before we implement it
    def print_formated_output(status):
        print(F"The computer is {computer_choice}. You are {user_choice}. You {status}.")
    
    # tie
    if user_choice == computer_choice:
        print_formated_output("tie")

    # user wins
    elif ((user_choice == "paper" and computer_choice == "rock") or 
          (user_choice == "rock" and computer_choice == "scissor") or
          (user_choice == "scissor" and computer_choice == "paper")):
        print_formated_output("win")

    # computer wins
    else:
        print_formated_output("lose")