# Can use this to filter out some elements while we are putting them
# into a new list using comprehensions

# ages = [22, 35, 27, 21, 20]
# odds = [age for age in ages if age % 2 == 1]

# print(odds)

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

# Comprehention Time:
present_friends = [
    name.title()                        # new thing you want to put into list
    for name in guests                  # iteration over an existing iterable
    if name.lower() in friends_lower    # the comprehension
]

print(present_friends)

# Output this way is in the order. Order NOT contained if sets were used.

# NEVER Nest list comprehensions inside one another