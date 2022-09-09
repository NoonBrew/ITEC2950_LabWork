from datetime import datetime

def main():
    # Main function that handles messaging
    GreetingMessage()

def GreetingMessage():
    # Asks for name input.
    name = input('Please Enter your name: ')
    # Prints the name entered and how many letters are in their name
    print('Greetings, {}, has {} letters!'.format(name.capitalize(), len(name)))
    # Asks for them to input a birthday month.
    birthdayMonth = input('{}, what month is your birthday? '.format(name.capitalize()))
    # This variable is here to hold a potential number if the user enters a number birthday month in stead of a string.
    numberBirthday = 0
    # If they value entered is numeric we assume it is an Int and convert it to an int value
    if birthdayMonth.isnumeric():
        numberBirthday = int(birthdayMonth)
        
    # Checks to see if the Int value is equal to the Int value of the month, 0 is safe because no month is the 0 month
    # Or checks to see if they capitalized version of the string is equal to the string format of the time now.
    if numberBirthday == datetime.now().month or birthdayMonth.capitalize() == datetime.now().strftime('%B'):
        print('It is your birthday month!!')
    else:
        print('It is not your birthday Month!')


main()
