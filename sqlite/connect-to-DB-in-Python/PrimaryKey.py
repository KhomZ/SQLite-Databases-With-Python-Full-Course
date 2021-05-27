# _________________________________________________________________________________________________________
# Part 6
# _________________________________________________________________________________________________________
# Primary Key ID
# it's a unique id no.
# @Khom


import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()

# Query The Database
c.execute("SELECT rowid, * FROM customers")


items = c.fetchall()

# print(items)
for item in items:
    print(item)



# # let's use loop now

# print("NAME " + "\t\tEMAIL")
# print("------" + "\t\t----------")
# for item in items:
#     # print(item)
#     print(item[0] + " " + item[1] + "\t" + item[2])  # formatting


# print("Command executed succesfully...")
# commit our command 
conn.commit()

# close our connection 
conn.close()