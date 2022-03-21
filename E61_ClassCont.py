my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99]
}

def average_grade(student):
    grades = student['grades']
    return sum(grades) / len(grades)


class Student:
    def __init__(self, new_name, new_grades): # self is the empty object that runs BEFORE the function
        self.name = new_name         # self.name is creating a new variable called name that lives inside of the blank object called self
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

print(student_one.name)
print(student_two.name)

print(student_one.average())