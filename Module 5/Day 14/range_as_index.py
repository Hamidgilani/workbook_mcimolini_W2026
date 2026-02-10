# range() is a handy tool for looping through a list if we want to use the index
letters = ["a", "b", "c", "d", "e", "f"]
print(letters)

# we can use range() to step through our list instead of checking every item
# like we do with a regular for loop

for num in range(len(letters)): # this will iterate 0 - 5 (our indexes)
    letters[num] = "z" # having access to the index when iterating, lets us edit our list in-place

print(letters)

letters = ["a", "b", "c", "d", "e", "f"]

# we can use this to get every other value in our list
for num in range(0, len(letters), 2):
    print(letters[num])