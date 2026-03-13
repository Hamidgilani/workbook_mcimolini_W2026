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
    "johan":"pineapple"
}

voting_results = {
    "banana": 0,
    "apple": 0,
    "orange": 0
}

print("Voters:")
for voter in fav_fruit_voters.keys():
    print(f"- {voter.title()}") # .title() capitalize the first word

# Tally up the votes with .values()
for vote in fav_fruit_voters.values():
#    match vote: 
#       case "banana":
#            voting_results["banana"] += 1
#        case "apple":
#            voting_results["apple"] += 1 
#        case "orange":
#            voting_results["orange"] += 1  
    voting_results[vote] = voting_results.get(vote,0) + 1 # as all of our values are keys in our dictionary, we can use them directly instead of using a 
# print out the votes
print("Voting Results:")
#print(voting_results)            

# We can do better using .items()
for fruit, vote_count in voting_results.items():
    print(f"- The fruit: {fruit} has {vote_count} votes")

