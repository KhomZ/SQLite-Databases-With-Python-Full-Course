# _________________________________________________________________________________________________________
# Part 4
# _________________________________________________________________________________________________________
# Query and Fetchall
# @Khom


import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()

# Query The Database
c.execute("SELECT * FROM customers")

# print(c.fetchone())
# print(c.fetchone()[0]) # this will give the first value only
# print(c.fetchmany(3))

# print(c.fetchall())
items = c.fetchall()

print(items)


# print("Command executed succesfully...")
# commit our command 
conn.commit()

# close our connection 
conn.close()