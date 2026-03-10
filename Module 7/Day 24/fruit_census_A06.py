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
    "johan": "pineapple"
}

voting_results = {
    # "banana": 0,
    # "apple": 0,
    # "orange": 0
}

print("Voters:")
for voter in fav_fruit_voters.keys():
    print(f"- {voter.title()}") # .title() capitalizes the first word

# Tally up the votes with .values()

for vote in fav_fruit_voters.values():
# This code is pretty complicated for what it does, and can be significantly reduced
#     match vote:
#         case "banana":
#             voting_results["banana"] += 1
#         case "apple":
#             voting_results["apple"] += 1
#         case "orange":
#             voting_results["orange"] += 1
    if vote in voting_results.keys(): # can use keys to error check our input
        voting_results[vote] += 1 # as all of our values are keys in our dictionary, we can just use them directly instead of using a match
    else:
        voting_results[vote] = 1

# Print out the votes
print("Voting Results:")
# print(voting_results) Let's do better
# We can do better using .items()
for fruit, vote_count in sorted(voting_results.items()): # Can use sorted() to sort our dictionary by key
    print(f"- The fruit: {fruit.title()} has {vote_count} votes")