print("Golf Score Calculator")

count = 0 
total_score = 0

is_active = True # this will be our flag

while is_active: # while our flag is True do...
    user_input =input("What was your most recent golf score ? (Type 'quit' to stop) ")
    if user_input == 'quit':
        is_active = False # Our while loop will exit the next timw we return to the top 

# We can do another way 
# while True:
    # if user_input =='quit':
        # break 
    else:
        total_score += int(user_input)
        count +=1

print(f"Your average golf score is {total_score/count}")
