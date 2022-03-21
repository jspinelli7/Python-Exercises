# Sets are useful = easy to compare

"""
art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)

science_but_not_art = science_friends.difference(art_friends)

print(art_but_not_science)
print(science_but_not_art)

not_in_both = art_friends.symmetric_difference(science_friends)

print(not_in_both)

art_and_science = art_friends.intersection(science_friends)

print(art_and_science)

all_friends = art_friends.union(science_friends)

print(all_friends)
"""

# Recap
# Difference does elements that are in one but not the other
# Symmetric Difference does elements that are not in both
# Intersection does elements that are in both
# Union gives all elements (Jen only once bc sets != duplicates)

# Mainly use Lists and Tuples
# Sets are reserved for when you need these operations

# Exercise:
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
new_friend = input('Enter the name of your friend: ')
# Add the name to the empty set
user_friends.add(new_friend)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print(nearby_people.intersection(user_friends))