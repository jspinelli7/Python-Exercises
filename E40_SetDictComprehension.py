friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}

print(present_friends)

# Although this method is a little bit longer it does have the advantage
# over E39 because sets remove any duplicates (eg. if there was a duplicate name.)

# This Episode proves you can do List Comprehension with sets & Dictionaries
# by using curly brackets instead of square

# Creates a dictionary using dictionary comrephension:
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))        # total of 4 inclusive
    if time_since_seen[i] > 5
}

print(long_timers)