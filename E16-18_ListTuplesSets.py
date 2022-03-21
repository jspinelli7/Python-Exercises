"""
friends = [
    ["Rolf", 24],
    ["Bob", 30],
    ["Anne", 27],
]

friends.remove(["Anne", 27])
print(friends)
"""

"""
short_tuple = "Rolf", "Bob"
a_bit_clearer = ("Rolf", "Bob")
tuple_in_list = [("Rolf", "Bob")]

# Lists you can add and remove elements
# Tuples you cannot.
# To add to a tuple, you can create another:

friends = ("Rolf", "Bob", "Anne")
friends = friends + ("Jen",)
print(friends)
"""

# Lists = []
# Tuples = () or no brackets
# Sets = {}

# Sets don't hold Order or contain Duplicate Elements
art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")

print(art_friends)

art_friends.add("Jen")

print(art_friends)

art_friends.remove("Jen")

print(art_friends)