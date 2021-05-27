# __________________________________________________________________________________________________________________
# Part 2
# __________________________________________________________________________________________________________________
# Insert One Record Into The table

import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()

c.execute("INSERT INTO customers VALUES ('Khom', 'Magar', 'khom@ikhomkodes.com')")
c.execute("INSERT INTO customers VALUES ('Kyzen', 'Smith', 'kyzen@ikhomkodes.com')")
c.execute("INSERT INTO customers VALUES ('Biraj', 'Thapa', 'biraj@ikhomkodes.com')")

print("Command executed succesfully...")
# commit our command 
conn.commit()

# close our connection 
conn.close()