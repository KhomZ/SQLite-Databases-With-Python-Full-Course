# @Khom
# ____________________________________________________________________________________________________________
# Part 1>>>
# ____________________________________________________________________________________________________________
# Create databse and table

import sqlite3

# conn = sqlite3.connect(':memory')
# creating database
conn = sqlite3.connect('customer.db')

# create a cursor 
c = conn.cursor()

# now creating a database table
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text

)""")

# sqlite has five datatypes : 
# 1. NULL(doesn't exist), 
# 2. INTEGER(a whole number), 
# 3. REAL(decimals), 
# 4. TEXT(simply text) & 
# 5. BLOB(stored exactly as it is like music mp3, image might be a blob) 

# commit our command 
conn.commit()

# close our connection 
conn.close()