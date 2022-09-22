import sqlite3

db = 'records.db'

def setup_database():
    create_table_sql = 'CREATE TABLE IF NOT EXISTS recordHolders (name text, country text, catches int)'

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

    with sqlite3.connect(db) as conn:
        conn.execute(add_record_sql, (name, country, catches))
    conn.close()

def search_by_name(name):

    search_by_name_sql = 'SELECT * FROM recordHolders WHERE name = ?'

    conn =  sqlite3.connect(db)
    results = conn.execute(search_by_name_sql, (name, ))
    first_name_result = results.fetchone
    conn.close()

    return first_name_result

def update_catches_by_name(name, new_catches):

    update_catches_sql = 'UPDATE recordHolders SET catches = ? WHERE name = ?'

    with sqlite3.connect(db) as conn:
        conn.execute(update_catches_sql, (name, new_catches))
    conn.close()

def delete_record_by_name(name):

    delete_sql = 'DELETE recordHolders WHERE name = ?'

    with sqlite3.connect(db) as conn:
        conn.execute(delete_sql, (name, ))
    conn.close()
