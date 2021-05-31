# _________________________________________________________________________________________________________
# Part 12
# _________________________________________________________________________________________________________
# Limiting Results
# @Khom


import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()


# Query The Database - Limiting the Results
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 4") # this is for AND i.e. intersection
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 4") # this is for OR i.e. Union
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 4 OR email LIKE '%ikhomkodes.com'")
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")


items = c.fetchall()

# print(items)
for item in items:
    print(item)



conn.commit()

# close our connection 
conn.close()