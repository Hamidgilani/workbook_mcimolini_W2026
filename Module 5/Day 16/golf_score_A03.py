print("Golf Score Calculator")

count = 0
total_score = 0 # This will track our total through each iteration of our loop
is_active = True # A flag to track when we should exit the loop

# Flag Example
# # I want my program to loop until is_active is False
# while is_active:
#     user_input = input("What was your most recent golf score? (Type 'quit' to stop) ")

#     # Generally, we want to check our exit condition as early as possible so we're sure it's covered
#     if user_input.lower() == "quit":
#         is_active = False
#     else: # increase our score and count
#         total_score += int(user_input)
#         count += 1

# print(f"Your average golf score is {total_score / count}.")

# Break Example
# I want my program to loop until it breaks
# A break loop will always execute at least once much like a Do-While loop
while True: # This will cause an infinite loop if I don't break.
    user_input = input("What was your most recent golf score? (Type 'quit' to stop) ")

    # Generally, we want to check our exit condition as early as possible so we're sure it's covered
    if user_input.lower() == "quit":
        break # This exits out of my while loop. Loop is infinite if this isn't reachable.
    else: # increase our score and count
        total_score += int(user_input)
        count += 1