numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

# Old way:
"""
for number in numbers:
    doubled_numbers.append(number * 2)
    
print(doubled_numbers)
"""


# doubled_numbers = [_ * 2 for _ in numbers]
# print(doubled_numbers)

"""
# Brackets signalize that you are creating a new list below - for loop
friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

print(age_strings)
"""

"""
names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)
"""

friend = input("Enter your friend's name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")

# Title casing is the normal case used for names. dot.title()



