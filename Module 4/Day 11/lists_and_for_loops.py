days_of_the_week = ["Sunday",
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"]

weekend_days = ("Saturday", "Sunday") # We can't edit this list once it's created

print(f"Our list: {days_of_the_week}")

print("Days of the week are: ")
for day in days_of_the_week:
    if day in weekend_days:
        print(f"{day} is a weekend day!")
    else:
        print(f"{day} is a week day :(")

# enumerate(List) returns both the index and the value at that index from our list
for index, day in enumerate(days_of_the_week):
    print(f"{day} is day number {index + 1} of the week") # Adding 1 as our index starts at 0

for day in days_of_the_week:
    if "u" in day: # strings are just fancy lists, so we can use in to check for content inside of them
        continue # continue skips the current list item and goes to the next
    print(f"{day} does not contain a 'u'")

for day in days_of_the_week:
    if day == "Wednesday":
        break # break will end execution of our loop
    print(f"{day} comes before Wednesday")