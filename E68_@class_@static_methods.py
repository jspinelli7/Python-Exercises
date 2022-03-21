class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


rolf = Student('Rolf', 'MIT')

rolf.marks.append(78)
rolf.marks.append(99)

print(rolf.average())

# An Instance method takes the caller as the first arguement
# A Class method takes the caller's class as the first arguement
# A Static method takes nothing as the first arguement

# example just to show syntax: these are terrible examples
class Foo:
    @classmethod        # used when you want something that wants to have access to the class
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod       # used when you want a method here that doesn't use the current object or the class
    def hi():               # but is somehow related to the class
        print('Hello, I don\'t take parameters.')

another_object = Bar()
another_object.hi()

