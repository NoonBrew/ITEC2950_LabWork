#Dataclass requires an additonal import
from dataclasses import dataclass

@dataclass
class Student:
    # Dataclass does not require a call to self when initalizing the variables for the object
    # Dataclass also requires the expected variables to be type cast so the user know what types of value
    # is expected when creating an object.
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'Name: {self.name}, ID: {self.school_id} GPA: {self.gpa}'


def main():

    alex = Student('Alex', 'abcdefg', 3.2) 

    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 1243123 , '2.3')
    print(sam)
    print(type(sam.gpa))

if __name__ == '__main__':
    main()