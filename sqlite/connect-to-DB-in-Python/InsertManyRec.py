# _________________________________________________________________________________________________________
# Part 3
# _________________________________________________________________________________________________________
# Insert Many Records Into The table

import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()

many_customers = [
                    ('Wes', 'Brown', 'wes@brown.com'), 
                    ('Kim', 'Pas', 'kim@pas.com'), 
                    ('Jim', 'Ale', 'jim@ale.com'),
                ]


c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)


print("Command executed succesfully...")
# commit our command 
conn.commit()

# close our connection 
conn.close()
