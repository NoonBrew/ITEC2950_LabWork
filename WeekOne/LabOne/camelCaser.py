"""
Modified Code for Week 3
Added this header because I was having conflicting repos
with the ProjectOne repo that was previously in a sub directory.
"""
def main():
    banner()
    instructions()
    # Ask for a string to convert
    stringToCamelCase = input('Enter your sentence: ')

    # Pass string to converter function
    ccStrign = ccConverter(stringToCamelCase)

    print(ccStrign)

def banner():
    """ Display program name, using stars"""
    message = 'Awesome Camelcase Program!!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

def instructions():
    """Displays instructions for how to use the program"""
    print('Enter a sentence and this program will convert it to camelcase.')

def ccConverter(string):
    """ Function used to convert a sentence into a camecase variable name"""
    #Split String into a list of the indivdual words based on space
    listOfWords = string.split()
    # Holds modified words for join statement
    listToJoin = []
    
    stringRejoined = ''
    # Use eneumerate because we care about the first word in the list.
    for index, word in enumerate(listOfWords):
        # First word we force into lowercase to adhere to camelCase
        if index == 0:
            word = word.lower()
        # Ever other word we capitalize
        else:
            word = word.capitalize()
        # Append words to list for join
        listToJoin.append(word)
    # Return our words joined with no space
    return stringRejoined.join(listToJoin)

if __name__ == '__main__':
    main()