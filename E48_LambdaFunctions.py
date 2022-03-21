# Lambda functions are used to get inputs,
# do a small amount of processing and return outputs
# Not used for performing actions...


#normal function
# def divide(x, y):
#    return x / y

#lambda function
divide = lambda x, y: x / y

print(divide(10, 5))

#You can also call this function this way, but never do this...
(lambda x, y: x / y)(15, 3)

#Lambda functions can provide simplicity at times

 def average(sequence):
    return sum(sequence) / len(sequence)

#Don't do this, better to use regular function structure here...
# average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))
