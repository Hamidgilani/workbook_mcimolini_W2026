fav_fruit_voters = {
    "daniel": "apple",
    "jessica": "apple",
    "michael": "banana",
    "john": "banana",
    "jessie": "apple",
    "jim": "orange",
    "jenny": "apple",
    "jason": "orange",
    "joseph": "banana",
    "james": "orange",
    "mary": "apple",
    "melody": "banana",
    "jonah": "pineapple" # this item is not in our voting_results, so we get an error
}

voting_results = {
    "orange": 0,
    "apple": 0,
    "banana": 0
}

# We can loop through our dictionary using .keys() to just look at the keys.
print("Voters:")
for voter in fav_fruit_voters.keys():
    print(f"- {voter.title()}") #.title() uppercases the first word in a string.

# We can loop through our dictionary using .values() to just look at the values attached to the keys.

# Original:
# for vote in fav_fruit_voters.values():
#    if vote == "banana":
#        voting_results["banana"] += 1
#    elif vote == "apple":
#        voting_results["apple"] += 1
#    elif vote == "orange":
#        voting_results["orange"] += 1

# Refactoring the above with key access
# Let's add error checking using key()
for vote in fav_fruit_voters.values():
    if vote in voting_results.keys():
        voting_results[vote] += 1 # as our values from the first dictionary are the keys in our second, we can sum directly without a logic statement
    else:
        voting_results[vote] = 1

print("Voting Results:")
#print(voting_results)

# Better voting results with .items() to loop through both our key and value simultaneously
for fruit, votes in voting_results.items(): # fruits is key, votes is value
    print(f"- The fruit: {fruit} has {votes} votes")

# Let's print our list sorted with sorted()
print("Voting Results By Name:")
for fruit, votes in sorted(voting_results.items()): # sorts by key by default
    print(f"- The fruit: {fruit} has {votes} votes")

# We can sort by value. This is currently outside of the scope of this course
print("Voting Results By Value:")
for fruit, votes in sorted(voting_results.items(), key = lambda item: item[1]):
    print(f"- The fruit: {fruit} has {votes} votes")