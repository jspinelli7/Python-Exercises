# Inheritance Lecture



class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)          # super() is the parent class - so you dont need self.etc = etc
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 40


rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())
print(rolf.weekly_salary())

anna = Student('Anna', 'Oxford')
# print(anna.weekly_salary)     # Error bc no weekly_salary in Student class
