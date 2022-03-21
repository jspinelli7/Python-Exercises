friend_ages = {
    "Rolf": 25,
    "Anne": 37,
    "Charlie": 31,
    "Bob": 22,
}

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")

# .itmes() allows you to retrieve both the key and the value of the pair

# for name in friend_ages -> will default and return keys
# for age in friend_ages.values() -> will return values instead of keys