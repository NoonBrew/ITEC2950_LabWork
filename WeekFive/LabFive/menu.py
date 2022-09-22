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

    for record in list_of_records:
        print(record)


def add_new_record():
    name = str(input('Enter record holders name: '))
    country = str(input(f'Enter {name}\'s Country of origin: '))
    catches = int(input(f'Enter {name}\'s number of catches: '))

    records.add_records(name, country, catches)
    print('record added.')


def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?') 


def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 


if __name__ == '__main__':
    main()