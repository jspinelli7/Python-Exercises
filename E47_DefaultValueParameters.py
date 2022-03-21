def add(x, y=3):        # Y is defaulted to 3. Default values must go at the end. Cannot do (x=3, y)
    total = x + y       # if one
    return total

# print(add(5, 6))       # If you don't call second value, it defaults to y=3

print(add(x=3))
print(add(x=5, y=2))     # These are called named arguements
print(add(3, y=2))

# print(add(x=5, 2))     # cannot do this

# If one parameter has a default value
# all subsequent parameters must have default values as well

# sep is a named arguement
print(1, 2, 3, 4, 5, sep=" - ")     # instead of space, sep uses whatever string you like as separator

# When python defines a function,
# it also stores whatever the default values are At that time