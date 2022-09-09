class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        return f'Student name: {self.name}, ID: {self.school_id}, current GPA: {self.gpa:.2f}'

alex = Student('Alex', 'abalsa', 3.245)
print(alex.name)
print(alex.school_id)
print(alex)

sam = Student('Sam', 234223123, 3.2)
print(sam)