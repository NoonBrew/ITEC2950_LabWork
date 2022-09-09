print('Hello Capstone!')
# Variables
school = 'MCTC'
gpa = 3.7
studentsInClass = 22

# if-statements
if gpa == 4.0:
    print('Wow!!')
elif gpa > 3:
    print('Awesome')
else:
    print('cool!')

# if-elif-else

#lists

schools = ['MCTC', 'DCTC', 'North Hennepin Technical Collegbe']
if 'MCTC' in schools:
    print('MCTC is one of the schools in the list')

# Sort and Reverse, sort and reverse in place.
schools.sort()
print(schools)

schools.append('Century College')
print(schools)
schools.reverse() # Returns None
print(schools)

# in operator

# Strings
className = 'Software Development Capstone'
print(className.upper())
print(len(className))
print(className.split())
print(className.split('o'))

if 'Capstone' in className:
    print('This must be the capstone')

# Loops - for loops over range

for x in range(10):
    print(x)

# Loops for loop over sequence
for s in schools:
    print(s.upper())

for letter in school:
    print(letter*10)

data = [0] * 10 # Can be used to make empty data lists

print(data)

moreData = [None] * 10
print(moreData)

#While loops

# name = input('Enter your name')
# while len(name) == 0:
#     print('Please enter at least one character ')
#     name = input('Enter your name: ')

# nameTwo = input('Enter your name: ')
# while not nameTwo:
#     print('Please enter at least one character ')
#     nameTwo = input('Enter your name: ')

# True and False and None

startOfSemester = True
winter = False

if winter:
    print('Brr!!')
else:
    print('it is not winter')

# Dictionaries

classCodes = {2905: 'Capstone', 2560: 'Web', 2545: 'Java'}
for code in classCodes:
    print(code)
    print(classCodes[code])

for code, name in classCodes.items(): # Returns a tuple of the key value
    print('The class code is {} and the name is {}'.format(code, name))

# Slicing Strings, Lists

firstTwo = schools[0:2]
print(firstTwo)

schoolName = 'Minneapolis Community and Technicale College'
city = schoolName[:11]
print(city)

lastSchool = schools[-1]
print(lastSchool)

lastTwoSchools = schools[-2:]
print(lastTwoSchools)

#file IO

with open('data.txt') as f:
    print(f.read())

with open('schools.txt', 'w') as f:
    for school in schools:
        f.writelines(school + '\n')

# Functions

def get_name():
    print('Hello please entet your name!')
    name = input('Your name is: ')
    return name

name = get_name()