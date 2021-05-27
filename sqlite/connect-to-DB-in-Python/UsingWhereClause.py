# _________________________________________________________________________________________________________
# Part 7
# _________________________________________________________________________________________________________
# Where Clause and how to use it?
# it's specifically used for searching some things in the database
# @Khom


import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()

# Query The Database
# c.execute("SELECT * FROM customers WHERE last_name = 'Magar'") 
# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%' ") 
c.execute("SELECT * FROM customers WHERE email LIKE '%ikhomkodes.com' ") 
# c.execute("SELECT * FROM customers WHERE email LIKE '%ale.com' ") 



# if numbers are to be compared then you can use id < ? i.e comparing operators are used e.g <, >, <=, >=, etc
# c.execute("SELECT * FROM customers WHERE age > 21") # eg query 


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