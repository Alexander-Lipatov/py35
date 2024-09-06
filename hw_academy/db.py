import sqlite3


conn = sqlite3.connect('database.db')

cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
            userid INT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            gender TEXT);
            """)

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()

cur.execute("""INSERT INTO users(userid, first_name, last_name, gender) 
   VALUES('00001', 'Alex', 'Smith', 'male');""")
conn.commit()

cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)

# class Test:

#     def __new__(cls) -> Self:
#         print(new)