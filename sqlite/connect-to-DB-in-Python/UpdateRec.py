# _________________________________________________________________________________________________________
# Part 8
# _________________________________________________________________________________________________________
# Update Records in a database
# now we will be learning to update the records of the database
# @Khom


import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()

# Update Records

# c.execute("""UPDATE customers SET first_name = 'Jimmy'
#             WHERE last_name = 'Ale'
#    """)
# let's not update the database like this because there may be many names whose last_name is "Ale". 
# so, be careful, use rowid instead
c.execute("""UPDATE customers SET first_name = 'Jim'
            WHERE rowid = 6
   """)
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