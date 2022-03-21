# Purpose of arguments and parameters is to make our functions
# generic so that we can use them with multiple difference pieces of data
# This is a car dictionary:

# car = {
#    "make": "Ford",
#    "model": "Fiesta",
#    "mileage": 23000,
#    "fuel_consumed": 460
# }

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]


def calculate_mpg(x, intro):
    print(intro)
    mpg = x["mileage"] / x["fuel_consumed"]
    name = f"{x['make']} {x['model']}"
    print(f"{name} does {mpg} miles per gallon.")

for car in cars:
    calculate_mpg(car, "New car:")

# Argument - value you pass in to the function
# Parameter - variable that accepts a value inside the function

# Good Practice: Give functions names that describe what they do - can easily tell what its doing