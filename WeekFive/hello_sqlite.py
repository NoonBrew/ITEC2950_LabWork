import sqlite3

connection = sqlite3.connect('first_db.sqlite') # Connects or creates new DB (Creates if DB does not exist.)
# conn.row_factory = sqlite3.Row ... what dis do?

connection.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')

# Commented out to not add new data to database.
# connection.execute('INSERT INTO products values (1000, "hat")')
# connection.execute('INSERT INTO products values (1001, "jacket")')
# connection.execute('INSERT INTO products values (1002, "socks")')

connection.commit() # required to commit

results = connection.execute('SELECT * FROM products')

# all_items = results.fetchall()
# print(all_items)

for row in results:
    print(row)

new_id = int(input('Enter new id: '))
new_name = input('enter new product name: ')

connection.execute('INSERT INTO products Values(?, ?)', (new_id, new_name)) # Parameterized insert 
# DO NOT USE f string formatting for inserts, updates, or deletes. It can lead to SQL injection
connection.commit()

update_product = 'wool hat'
update_id = 1000
connection.execute('UPDATE products SET name = ? WHERE id = ?', (update_product, update_id))
connection.commit()

delete_prodcut = 'pants'
connection.execute('DELETE from products WHERE name = ?', (delete_prodcut, )) # extra comma needed to maintain tuple identity?
connection.commit()

connection.close()
