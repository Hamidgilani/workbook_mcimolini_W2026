grades = [72, 51, 96, 80, 63]

print(f"Grades: {grades}")

# Sorts our list low to high. Changes our list in place.
grades.sort()
print(f"Sorted Grades: {grades}")

# Sorts our list hight to low. Also changes in place.
grades.sort(reverse=True)
print(f"Reverse Sorted Grades: {grades}")

# Add an item to the end of the list with .append()
grades.append(100)
print(f"New Grades: {grades}") # added to the end regardless of previous sorting

grades.sort() # Just because

# We can add an item to a specific location in our list with .insert(index, value)
# If index doesn't exist we'll get an IndexError
grades.insert(2, 66)
print(f"Inserted list: {grades}")

# Really Really bad idea, but can be done in python
grades.insert(4, "apple")
print(f"Bad list: {grades}")

# .remove(vale) lets me take out items I don't want from my list
# .remove() does not return the item removed from the list
item_removed = grades.remove("apple")
print(f"Good list: {grades}")
print(f"Item removed: {item_removed}")

# .pop(index) removes and returns the item. Throws IndexError if index is invalid
item_removed = grades.pop(len(grades) - 1)
print(f"Shrunk list: {grades}")
print(f"Item removed: {item_removed}")

# .remove() only removes the first instance of the value
grades.append(item_removed) # Adds 100 to the end
grades.append(item_removed) # Adds a second 100 to the end
grades.remove(item_removed) # Removes the first 100
print(f"Fixed list: {grades}")

# We can use in to determine if something is inside our list
# This will return a boolean value (True or False; 0 or 1)

if 100 in grades:
    print("Someone got a perfect score!")
else:
    print("Whomp whomp")

# We can store the output of in as a variable
# We can technically store the return value from any comparison opperation (==, !=, >, <, etc)
is_perfect_score = 100 in grades # Equates to True

if is_perfect_score:
    print("Yay!")

is_grade_zero = 0 in grades # Equates to False

if is_grade_zero:
    print("Someone got a 0?!?")