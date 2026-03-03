import random

# Function definitions (defs) should be at the top of your file after any imports
def convert_input_to_result(number):
    result = ""
    if number == 0:
         result = "scissor"
    elif number == 1:
         result = "rock"
    elif number == 2:
         result = "paper"     
    return result 

def check_result(result_1,result_2):
      # You can define functions in functions aka helper functions
      def print_result(outcome):
          print(F"The computer is {result_2}. You are {result_1}. {outcome}.")
      #tie
      if result_1 == result_2:
        print_result("It is a draw")
      # user wins
      elif ((result_1 == "paper" and result_2 == "rock") or 
         (result_1 == "rock" and result_2 == "scissor") or
         (result_1 == "scissor" and result_2 == "paper")):
         print_result("You win")
        # computer wins
      else:
       print_result("You lose")

