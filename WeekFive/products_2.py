import sqlite3

# valdation erros, rowid

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT UNIQUE, quantity INT)')
conn.close() # Not sure if this is needed with a with resource block.

name = 'scarf'
quantity = 3

try:
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.close() # again not sure if needed. 
except Exception as e:
    print('Error inserting ', e)

conn = sqlite3.connect(db)
results = conn.execute('SELECT * FROM products')
for row in results:
    print(row)