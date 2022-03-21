# This is my main python file for all of the practice examples within the Udemy Course

"""
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)

print(f"My friends are {comma_separated}.")
"""


"""
friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
  print("Hello, friend!")
else:
  print("Hello, stranger!")
  """

"""
name = input("Enter your name: ")

if name:
  print("We know your name.")
else:
  print("Please enter your name")
"""

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
  print("Hello, friend.")
elif user_name in family:
  print("Hello, family.")
else:
  print("I don't know you.")
