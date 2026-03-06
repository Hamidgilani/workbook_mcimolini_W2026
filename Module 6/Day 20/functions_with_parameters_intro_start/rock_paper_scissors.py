import random

user_input =  int(input("Scissor (0), rock (1), paper (2): "))
computer_input = random.randint(0, 2)

user_result = ""
if user_input == 0:
    user_result = "scissor"
elif user_input == 1:
    user_result = "rock"
elif user_input == 2:
    user_result = "paper"

computer_result = ""
if computer_input == 0:
    computer_result = "scissor"
elif computer_input == 1:
    computer_result = "rock"
elif computer_input == 2:
    computer_result = "paper"

# tie
if user_result == computer_result:
    print(F"The computer is {computer_result}. You are {user_result}. It is a draw")
# user wins
elif ((user_result == "paper" and computer_result == "rock") or 
    (user_result == "rock" and computer_result == "scissor") or
    (user_result == "scissor" and computer_result == "paper")):
    print(F"The computer is {computer_result}. You are {user_result}. You win")
# computer wins
else:
    print(F"The computer is {computer_result}. You are {user_result}. You lose")