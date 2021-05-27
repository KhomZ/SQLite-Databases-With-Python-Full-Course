# _________________________________________________________________________________________________________
# Part 10
# _________________________________________________________________________________________________________
# Order Results By
# @Khom


import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()


# Query The Database - ORDER BY
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid") # by default it's ASCending order
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC") 
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name")  # by default it's ASCending order
c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")



items = c.fetchall()

# print(items)
for item in items:
    print(item)



conn.commit()

# close our connection 
conn.close()