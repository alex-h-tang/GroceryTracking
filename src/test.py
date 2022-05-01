import sqlite3

conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
product_id = 4001
urls= conn.execute('select * from "vUrlDetails" where product_id = ?', (product_id,)).fetchall()
conn.close()
if urls:
    for url in urls:
        print( url['store'], url['url'], url['name'])

