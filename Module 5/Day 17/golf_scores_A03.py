print("Golf Score Calculator")
count = 0
total_score = 0
# removed active variable

while True:
    user_input = input("What was your most recent golf score? (enter 'quit' to stop) ")
    if user_input == 'quit': # quit if the user enters 'quit'
        break
    else: # add the score to the total and increment the count
        is_valid = True
        try:
            total_score += int(user_input)
        except ValueError as error_message: # very common for this variable to just be e
            print(f"Could not convert input to a number. {error_message}")
            is_valid = False
        
        if is_valid:
            count += 1
# use the average.
try:
    average = total_score / count
    print(f"Your average golf score is {average}.")
except ZeroDivisionError:
    print("You didn't enter any scores!")

# this could equally be an if/else
if count == 0:
    print("You didn't enter any scores!")
else:
    average = total_score / count
    print(f"Your average golf score is {average}.")

