

def yourClasses():
    # variable with empty list
    classList = []
    # Asks the user how many classes they are taking so we know how long the list is going to be.
    classTot = input('How many class are you taking this semester? ')
    # Use a while loop to make sure user enters a postive number
    while not classTot.isnumeric() or int(classTot) < 0:
        print('Please enter a positive number. ')
        classTot = input('How many class are you taking this semester? ')
    # For loop runs for how ever many classes they are taking
    for c in range(int(classTot)):
        # asks the user to enter a class in one by one
        className = input('Enter the name of class {}: '.format(c +1))
        # Appends that class to the list
        classList.append(className.capitalize())
    
    # Uses another for loop to print each class one by one. 
    print('The classes you are taking are:')
    for c in classList:
        print(c)


yourClasses()