'''Lab 2 Part 1 and Part 2'''

class Author:
    # Init function, set books default value to an empty list.
    def __init__(self, name):
        self.name = name
        self.books = []

    # Function to append books to the list
    def publish(self, book):
        if book in self.books:
            print(f'Error: {book} is already in the list.')
        else:
            self.books.append(book)

    def __str__(self):
        book_list = ', '.join(self.books) or 'No published books'
        return f'the author, {self.name}, has published the following books: {book_list}.'

def main():

    author_one = Author('J.R.R Tolkein')

    author_one.publish('Fellowship of the Ring')
    author_one.publish('The Two Towers')
    author_one.publish('Return of the King')

    print(author_one)

    author_one.publish('Fellowship of the Ring')

    print(author_one)

    author_two = Author('Nate O')

    print(author_two)


main()