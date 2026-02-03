grades = [87, 53, 18, 29, 94]
print(f"Grades: {grades}")

# Sort our list. This happens in-place aka. once you call sort it stays sorted until you change the list
# This sorts low to high by default (a -> z; 0 -> 9)
grades.sort()
print(f"Sorted grades: {grades}")

# We can reverse sort as well
grades.sort(reverse=True)
print(f"Reverse sorted grades: {grades}")

# We can add items to our list
# .append(value) adds our value to the end of the list
grades.append(100)
print(f"Longer list: {grades}") # 100 ends up at the end of the list, even though it should be the 1st item if sorted

# If I want this sorted, I will have to sort again.
grades.sort()

# .insert(index, value) adds an item at a specific index, then shifts every other item "right"
# Very handy way to add things when your list is already sorted or grouped in some way
grades.insert(3, 57)
print(f"Grades after instert: {grades}")

# We can remove items from our list with .pop(index) or .remove(value)
# .pop(index) will return the value removed
popped_grade = grades.pop(3) # Don't have to save the value to a variable, but I can
print(f"Shortened list: {grades}")
print(f"Popped: {popped_grade}")

# .remove(value) takes out/removes/deletes/etc the FIRST INSTANCE of it's value
# if our value doesn't exist in the list, then we get a ValueError
grades.append(100)
print(f"Grades before remove: {grades}") # 100 is here twice

grades.remove(100)
print(f"Grades after remove: {grades}") # only 1 100 left

# To make remove safe, we need to check if the value we want to remove exists first
# We can do that with 'in'
# 'in' will search our list for a value and return True if it's found; False otherwise
top_grade = 100

if 0 in grades:
    print("Someone got 0?!?") # Will only print if the value 0 is in grades
elif top_grade in grades:
    print("Someone scored 100!!!") # Will only print if the value 100 is in grades

# We can assign in statements to a variable (can do this with any comparator (==, !=, <, >, etc))
is_found = 100 in grades

if is_found:
    print("Huzzah!")