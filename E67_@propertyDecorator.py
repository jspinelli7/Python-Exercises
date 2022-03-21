class Student:
    def __init__(self, name, school):
        self.name = name            # name, school, marks are all called properties
        self.school = school        # Because the object now has this value defined inside of it
        self.marks = []             # Methods are functions inside of a class - functions do something or take some action

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)          # super() is the parent class - so you dont need self.etc = etc
        self.salary = salary

    @property               #the @property decorator turns this method into something that can be used like below... line 27
    def weekly_salary(self):        # you can change a simple no arguement method into a property (or accessed as if it were a property)
        return self.salary * 40


rolf = WorkingStudent('Rolf', 'MIT', 15.50)

#print(rolf.weekly_salary())     # here weekly_salary doesn't DO anything, it just returns a value

# if the funcion only takes a self arguement and isn't one that does things but
# rather just calculates a value based on self's properties, then...

print(rolf.weekly_salary) # if we want to do this we need to use whats called a decorator

# ***IMPORTANT*** If you are doing an action like connecting to a database or opening a file, any action, etc
    # DO NOT USE the @property decorator
        # ONLY use @property when calculating values from the object's property themselves (local)