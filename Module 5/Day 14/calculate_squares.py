print("Calculate squares for the following ranges:")

# range can be used with just range(end). End is exclusive. start defaults to 0.
for num in range(5):
    print(f"Iteration: {num} has a square of {num ** 2}") # ** is exponent; often ^ in other languages

# range can have a defined start as range(start, end). End is exclusive, start is inclusive
for num in range(2, 6):
    print(f"Iteration: {num} has a square of {num ** 2}") # ** is exponent; often ^ in other languages

# range can also take a step (the amount it counts by)
# range(start, end, step). end is exclusive, start is inclusive, count by step.
print("Calculate squares for the following ranges:")

# range can be used with just range(end). End is exclusive. start defaults to 0.
for num in range(2, 6, 2):
    print(f"Iteration: {num} has a square of {num ** 2}") # ** is exponent; often ^ in other languages

# we can print our range by casting to a list
print(list(range(2, 7, 2)))

# this does not print anything useful
print(range(2, 7, 2))