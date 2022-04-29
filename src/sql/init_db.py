import sqlite3

connection = sqlite3.connect('.\\src\\database.db')


with open('.\\src\\sql\\schema.sql') as f:
    connection.executescript(f.read())

with open('.\\src\\sql\\add_data.sql') as f:
    connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

connection.commit()
connection.close()