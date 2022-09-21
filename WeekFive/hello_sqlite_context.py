import sqlite3

db = 'first_db.sqlite'

def create_table():
    with sqlite3.connect(db) as connection:
        connection.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')
    connection.close()

def insert_example_data():
    with sqlite3.connect(db) as connection:
        # Commented out to not add new data to database.
        connection.execute('INSERT INTO products values (1000, "hat")')
        connection.execute('INSERT INTO products values (1001, "jacket")')
        connection.execute('INSERT INTO products values (1002, "socks")')
    connection.close()

def display_all_data():
    connection = sqlite3.connect(db)
    results = connection.execute('SELECT * FROM products')
    print('All products: ')
    for row in results:
        print(row) # Each row will be a tuple
    # all_items = results.fetchall()
    # print(all_items)
    connection.close()

def display_one_product(product_name):
    connection = sqlite3.connect(db)  
    results = connection.execute('SELECT * FROM products WHERE name like ?', (product_name, ))
    first_row = results.fetchone()
    if first_row:
        print('Your product is : ',  first_row) #upgrade to row factory later?
    else:
        print('not found')
    connection.close()

def create_new_product():
    
    new_id = int(input('Enter new id: '))
    new_name = input('enter new product name: ')
    with sqlite3.connect(db) as connection:
        connection.execute('INSERT INTO products Values(?, ?)', (new_id, new_name)) # Parameterized insert 
    # DO NOT USE f string formatting for inserts, updates, or deletes. It can lead to SQL injection
    connection.close()

def update_product():
    update_product = 'wool hat'
    update_id = 1000

    with sqlite3.connect(db) as connection:        
        connection.execute('UPDATE products SET name = ? WHERE id = ?', (update_product, update_id))
    connection.close()

def delete_product(product_to_delete):
    with sqlite3.connect(db) as connection:
        connection.execute('DELETE from products WHERE name = ?', (product_to_delete, )) # extra comma needed to maintain tuple identity?
    connection.close() # Still need to close the connection. 

create_table()
insert_example_data()
display_all_data()
display_one_product('coat')
create_new_product()
update_product()
delete_product('jeans')
