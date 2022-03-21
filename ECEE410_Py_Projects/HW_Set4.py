import cmath
"""
#Quadratic equation is ax**2+bx+c = 0

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

d = (b**2) - (4*a*c)

solution1 = (-b-cmath.sqrt(d))/(2*a)
solution2 = (-b+cmath.sqrt(d))/(2*a)

print(f"Your two solutions are {solution1} and {solution2}.")
"""



tri = "No you cannot make a Triangle."
tri2 = "Yes you can make a Triangle."

def user_inputs():
    a, b, c = [int(x) for x in input("Enter 3 stick lenths: ").split()]

def is_triangle(a, b, c):
    if a > b+c or b > a+c or c > a+b:
        print(f"{tri}")
    else:
        print(f"{tri2}")

user_inputs(is_triangle(a, b, c))
