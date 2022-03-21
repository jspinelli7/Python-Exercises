

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]


def calculate_mpg(x):
    mpg = x["mileage"] / x["fuel_consumed"]
    return mpg                              # As soon as Python encounters a return statement, the function ends


def car_name(x):
    name = f"{x['make']} {x['model']}"
    return name                             # When you return, you can assign that value to a variable


def print_car_info(x):
    name = car_name(x)
    mpg = calculate_mpg(x)
    print(f"{name} does {mpg} miles per gallon.")
    return None     # All functions in python return the value none by default. Means no value


for car in cars:
    print_car_info(car)

# Good Practice: Leave two lines between each function

# Functions can return multiple times

def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y

print(divide(10, 2))
print(divide(6, 0))