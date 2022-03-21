


currencies = 0.8, 1.2
usd, eur = currencies # turning values of tuple into multiple variables
                      # usd becomes 1.8 and eur becomes 1.2

friends = [
    ("Rolf", 25),
    ("Anne", 37),
    ("Charlie", 31),
    ("Bob", 22)
]

# for friend in friends

for name, age in friends:
    # print(name, age)
    print(f"{name} is {age} years old.")


"""
# old way of doing it
for friend in friends:
    name = friend[0]
    age = friend[1]
"""
