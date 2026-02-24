print("Golf Score Calculator")
count = 0
total_score = 0
# removed active variable

while True:
    user_input = input("What was your most recent golf score? (enter 'quit' to stop) ")
    if user_input == 'quit': # quit if the user enters 'quit'
        break
    else: # add the score to the total and increment the count
        is_valid = True # can use a flag to track an error and do something instead of using an else.
        try:
            total_score += int(user_input)
        except ValueError as error_message: # error_message is often shortened to e
            print(f"Could not convert input ({user_input}) to a number. {error_message}")
            is_valid = False
        
        if is_valid:
            count += 1

# use the average.
# there are 2 ways to fix/avoid/manage this error (Divide by zero)
# if way aka a "guard statement"
if count != 0:
    average = total_score / count
    print(f"Your average golf score is {average}.")
else:
    print(f"No scores entered. Have a nice day!")

# try way
try:
    average = total_score / count
    print(f"Your average golf score is {average}.")
except ZeroDivisionError:
    print(f"No scores entered. Have a nice day!")