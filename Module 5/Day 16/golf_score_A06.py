print("Golf Score Calculator")

count = 0
total_score = 0
is_active = True # this will be our flag

while is_active: # while our flag is True do....
    user_input = input("What was your most recent golf score? (Type 'quit' to stop) ")

    # We want to check our flag as early as possible
    if user_input == "quit":
        is_active = False # Our while loop will exit the next time we return to the top
    else:
        total_score += int(user_input) # adds score to running total
        count += 1 # tracks the number of scores added

# Same thing, but with True and break
while True: # This will run forever until we break out of the loop
    user_input = input("What was your most recent golf score? (Type 'quit' to stop) ")

    # We want to check our flag as early as possible
    if user_input == "quit":
        break # Our while loop will exit immediately
    else:
        total_score += int(user_input) # adds score to running total
        count += 1 # tracks the number of scores added

# Won't execute until we've exited our loop
print(f"Your average golf score is {total_score / count}")