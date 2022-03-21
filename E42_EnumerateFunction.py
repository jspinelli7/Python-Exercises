# enumerate is used to join this list with a number for each element in a list
# It will also join these together in a list so that we can access them

friends = ["Rolf", "John", "Anna"]

"""
counter = 0

for friend in friends:
    print(counter)
    print(friend)
    counter += 1
"""


# the enumerate function gives us the two values (counter & friend) for each of the values in the friends list
for counter, friend in enumerate(friends, start=1):     # start=1 argument makes enumerate start at 1 instead of 0
    print(counter)
    print(friend)

print(list(enumerate(friends)))     # This gives us the list of enumerate which is a list of tuples
print(dict(enumerate(friends)))     # This will turn these tuples into dictionary keys and value pairs