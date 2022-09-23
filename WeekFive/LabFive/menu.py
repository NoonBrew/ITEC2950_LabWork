"""
A menu - you need to add the database and fill in the functions. 
"""
import records

def main():

    records.setup_database()

    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    list_of_records = records.show_all_records()

    # Break the tuple apart so I can format the output to look a little nicer than just rows of tuples.
    for name, country, catches in list_of_records:
        print(f'Name: {name}, Country: {country}, Catches: {catches}')


def add_new_record():
    name = str(input('Enter record holders name: '))
    country = str(input(f'Enter {name}\'s Country of origin: '))
    catches = int(input(f'Enter {name}\'s number of catches: '))

    # Result is either a number or None which is the same as false. If it is false we will print a statment
    # Letting the user know the record was not added. 
    result = records.add_records(name, country, catches)
    if not result:
        print(f'A record for {name} already exists and was not added again')
    else:
        print('A record has been added.')


def edit_existing_record():
    name = str(input('Enter name to update: '))
    new_catches = int(input(f'Enter new number for {name}: '))
    records_updated = records.update_catches_by_name(name, new_catches)
    if records_updated < 1:
        print(f'Record for {name} was not found.')
    


def delete_record():
    name = str(input('Enter name of record to delete: '))
    records_deleted = records.delete_record_by_name(name)
    if records_deleted < 1: 
        print(f'No record with {name} was found.')


if __name__ == '__main__':
    main()