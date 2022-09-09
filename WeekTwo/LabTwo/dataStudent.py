#Dataclass requires an additonal import
from dataclasses import dataclass

@dataclass
class Student:
    # Dataclass does not require a call to self when initalizing the variables for the object
    # Dataclass offers type hints when you create an object.
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'Name: {self.name}, ID: {self.school_id} GPA: {self.gpa}'


def main():

    # Dataclasses seem great when you want to just make something objects to hold data for access. 
    # The set up seems more streamlined. 
    alex = Student('Alex', 'abcdefg', 3.2) 

    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 45342, 2.3)
    print(sam)

if __name__ == '__main__':
    main()


