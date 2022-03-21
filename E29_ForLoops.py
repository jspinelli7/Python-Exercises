
"""
friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)
"""

# elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for index in range(2, 20, 3):
#    print(index)

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    # print(name + ', ' + str(grade))
    print(f"{name} has a grade of {grade}.")

# Use a For loop when you want to repeat something a certain number of times
# and you know how many that number of times is.
# OR you want to use each value of an iterable and you want to do something once
# for each of the values