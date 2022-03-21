"""
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
# Rolf is the key : 24 is the value

print("Rolf's age is " + str(friend_ages["Rolf"]))

# To add to dictionary
friend_ages["Bob"] = 20

friend_ages["Rolf"] = 25

print(friend_ages)

# Dictionaries keep order, but no duplicates
"""
"""
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)

print(friends[0]["name"])
"""

# Dict turns data into a Dictionary
# Here we hae a list of Tuples

friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend_ages = dict(friends)
print(friend_ages)

print(friend_ages["Rolf"])