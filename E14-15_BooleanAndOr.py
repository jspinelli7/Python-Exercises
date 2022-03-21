"""
age = 20
is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20

print(is_over_age)
print(is_under_age)
print(is_twenty)
"""

"""
my_number = 5
user_number = int(input("Enter a number: "))

matches = my_number == user_number

print(f"You got it right: {matches}.")
"""

# And/Or starts here

"""
age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}.")
"""

"""
age = int(input("Enter your age: "))
working = age >= 18 and age <= 65

print(f"At {age}, you are usually working: {working}.")
"""

name = input("Enter your first name: ")
surname = input("Enter your last name: ")

greeting = name or f"Mr. {surname}"
print(greeting)