"""
my_name = "Joseph"
your_name = input("Enter your name: ")

print(f"Hello {your_name}. My name is {my_name}.")
"""

# age = input("Enter your age: ")
# age_num = int(age)

"""
age = int(input("Enter your age: "))
months = age * 12
print(f"You have lived for {months} months.")
"""

# StringFormatting, E11 Below

my_string = """Hello, world.


My name is Joseph. Welcome to my program.
"""
print(my_string)

my_name = "Joseph"
age = 23
age_as_string = str(age)
first_string = "Hello, my name is: " + my_name + " and I am " + age_as_string + " years old."
print(first_string)

print(f"You are {age}")


final_greeting = "How are you, {}?"
joseph_greeting = final_greeting.format(my_name)
print(joseph_greeting)

bob_greeting = final_greeting.format("Bob")
print(bob_greeting)