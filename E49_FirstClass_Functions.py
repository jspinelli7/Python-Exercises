# Calling of the function happens when you use the brackets after function name
# If use just the function name, no output but still value
# greet - just gives the value of the function greet()
# We can then assign this value to a variable such as *hello
# First Class Citizen means you can assign it to variables or put it inside lists or dictionaries
# First Class function is a function you can pass to another funt as an arguement.
"""
def greet():
    print("Hello")

hello = greet

hello()
"""

#def average(seq):
#    return sum(seq) / len(seq)


avg = lambda seq: sum(seq) / len(seq)
total = sum #lambda seq: sum(seq)
top = max #lambda seq: max(seq)

#Use dictionaries to create associations:
operations = {
    "average": avg,
    "total": total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    operation_function = operations[operation] # this will get the ABC function itself, not the result of running the function
    print(operation_function(grades))          # If key doesnt exist - Can use error handling to print nice message instead of error

    """ if operation == 'average':
        print(avg(grades))
    elif operation == 'total':
        print(total(grades))
    elif operation == 'top':
        print(top(grades)) """

