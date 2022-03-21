friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]


# zip function to combine two lists into pairs
long_timers = dict(zip(friends, time_since_seen))


# turns them into a list of tuples [('Rolf',3), ('Bob', 7),....]
# long_timers = list(zip(friends, time_since_seen))

# zip ignores any elements that don't match the other lists ex. '5' is extra
# You will always end up with the shortest list
extra_list = list(zip(friends, time_since_seen, [1, 2, 3, 4, 5]))


print(long_timers)
print(extra_list)


guests = [('rolf', 25), ('adam', 28), ('jen', 24)]
print(dict(guests))