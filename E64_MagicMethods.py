# Magic Methods in Python
# Python automaticaly calls __init__ for example

class Student:
    def __init__(self, name):
        self.name = name

movies = ['Matrix', 'Finding Nemo']
print(movies.__class__) # prints the object type
print("hi".__class__)

print(len(movies))

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
       return len(self.cars)

    def __getitem__(self, item):    # MUST define this inorder to use a for loop in our class
        return self.cars[item]

    def __repr__(self):     # used to return out a string that represents the object
        return f'<Garage {self.cars}>'

    def __str__(self):      # used to return a string that tells user information about object
        return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford.cars))
print(ford[0])  # Garage.__getitem__(ford, 0)

for car in ford:        # must have __getitem__ defined
    print(car)

print(ford) #str gets called...if no str funct, then the repr will get called

# repr gets called when debugging