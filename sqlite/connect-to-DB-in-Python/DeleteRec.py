# _________________________________________________________________________________________________________
# Part 9
# _________________________________________________________________________________________________________
# Delete Records from a database
# now we will be learning to delete records of the database
# @Khom


import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()

# Delete Records
c.execute("DELETE from customers WHERE  rowid = 11")

conn.commit()



# Query The Database
c.execute("SELECT rowid, * FROM customers ") 


items = c.fetchall()

# print(items)
for item in items:
    print(item)



conn.commit()

# close our connection 
conn.close()