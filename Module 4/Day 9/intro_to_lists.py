groceries = ["lettuce", "tomatoes", "bread", "milk", "chicken", "apples"]

print("Our grocery list is: ")
print(groceries)

# List access starts at 0
# Print an item at an index
print("First item is: ")
print(groceries[0])

# List access in reverse starts at -1
print("Last item is: ")
print(groceries[-1])

# IndexErrors are thrown if we try to access an index that doesn't exist.
# print(groceries[42]) #would throw an IndexError

# We can change items at indexes
groceries[0] = "romaine lettuce"
print(groceries)

# We can slice lists with [start:end] start is inclusive, end is exclusive
print("First 3 items: ")
print(groceries[:3])

print("Last 2 items: ")
print(groceries[-2:])
print(groceries[4:6])

# len() is used to measure our list (count the number of items in it)
print(f"Our grocery list has {len(groceries)} items.")

print("The last 3 items are: ")
print(groceries[len(groceries) - 3 : len(groceries)])

# Can replace a hard coded index (0) with a variable
item = int(input("Select an item: "))
print(groceries[item])