import sqlite3
import os

# imported OS path to move to lab5 folder so Database would not be written in my week 5 folder. 
db = os.path.join('LabFive', 'records.db')

def setup_database():
    create_table_sql = 'CREATE TABLE IF NOT EXISTS recordHolders (name text UNIQUE, country text, catches int)'

    with sqlite3.connect(db) as conn:
        conn.execute(create_table_sql)
    conn.close()

def show_all_records():
    get_all_records_sql = "SELECT * FROM recordHolders"
    conn = sqlite3.connect(db)
    results = conn.execute(get_all_records_sql)
    all_records = results.fetchall()
    return all_records

def add_records(name, country, catches):

    add_record_sql = 'INSERT INTO recordHolders VALUES (?, ?, ?)'
    try:
        with sqlite3.connect(db) as conn:
            records_added =conn.execute(add_record_sql, (name, country, catches))
        conn.close()
        return records_added.rowcount
    except sqlite3.IntegrityError:
        return None


def search_by_name(name):

    search_by_name_sql = 'SELECT * FROM recordHolders WHERE name = ?'

    conn =  sqlite3.connect(db)
    results = conn.execute(search_by_name_sql, (name, ))
    first_name_result = results.fetchone
    conn.close()

    return first_name_result

# Update and Delete return a rowcount so we can check to see if anything was actually updated or deleted.
# If a record was not found the rowcount value will be 0 and will be used to generate a message
# In the menu.py file. 
def update_catches_by_name(name, new_catches):

    update_catches_sql = 'UPDATE recordHolders SET catches = ? WHERE name like ?'
    with sqlite3.connect(db) as conn:
        records_modified = conn.execute(update_catches_sql, (new_catches, name))
    conn.close()

    return records_modified.rowcount

def delete_record_by_name(name):

    delete_sql = 'DELETE FROM recordHolders WHERE name = ?'

    with sqlite3.connect(db) as conn:
        records_deleted = conn.execute(delete_sql, (name, ))
    conn.close()

    return records_deleted.rowcount
