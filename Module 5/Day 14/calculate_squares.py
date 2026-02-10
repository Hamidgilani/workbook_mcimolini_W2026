print("Calculate square for the following range")

for num in range(5): # range excludes the stop, so will end at 4. Start is 0 by default, Step is 1.
    print(f"Interation: {num} has a square of {num ** 2}") # ** is our exponent operator

# range can take a start: range(start, end). start is inclusive, end is exclusive
print("Starting at 2 to 5")
for num in range(2, 6): # this should print 2 - 5
    print(f"Interation: {num} has a square of {num ** 2}")

# range can take a step value: range(start, end, step). step will increase each iteration by itself
print("Stepping by 2")
for num in range(2, 6, 2): # this should print 2 and 4
    print(f"Interation: {num} has a square of {num ** 2}")

# if you're ever unsure of what will be in your range, you can convert to a list and print it.
print(list(range(2, 6, 2)))