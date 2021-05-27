# @Khom

import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()

# Query The Database
c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany()

print(c.fetchall())

# print("Command executed succesfully...")
# commit our command 
conn.commit()

# close our connection 
conn.close()


