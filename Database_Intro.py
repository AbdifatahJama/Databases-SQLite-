''''Currently, we have been using files such .csv .txt to save data

However, it is widely considered to be best practise to store data within scripts in databases

This folder we store data within the database using SQLITE(Structured Query Language)

SQLite is a relational database management system

A relational database organizes data into tables which can be linked—or related—based on data common to each.

Databases store many tables
SQL allows us to communicate with the DATABASE 
'''

'''SQL DATA TYPES

SQL have 5 main data types that can be used in database

1) Null
2) Interger
3) Real(Floating/decimal number)
4) Text (UTF format)
5) Blob (stored data excactly it is inputted)

Different data types have different size 
'''
'''Further more Databases have .db extension

To have the ability to open .db files we must use the URL: 
'''
import sqlite3
import csv
from sqlite3.dbapi2 import connect

# '''Create connection'''
# conn = sqlite3.connect('customers.db') # If database doesnt exist database is created 
# c = conn.cursor()

# '''Creating table within the database and adding data'''

# c.execute('''CREATE TABLE 
#           customers 
#           (First_Name TEXT,last_name TEXT,email TEXT,age INT)''')


# conn.commit() # commit/saves and push data into database
# conn.close()

##Inserting record into table
'''We need to connect to the database again and make cursor again
using INSERT INTO TABLE NAME VALUES command
'''

conn = sqlite3.connect('customers.db') # Makes a new connection with existing database
c = conn.cursor() # Creates cursor
c.execute('''INSERT INTO customers VALUES("Tim","James","TimJames@gmail.com",35)''') # Executes by adding data into table name 'customers'
print('EXECUTED')
conn.commit()
c.close()
conn.close()

'''Inserting lots of records into table'''

manyCustomer = [("Tim","Jack","TimJack@gmail.com",45),("Jack","Lane","JackLane@gmail.com",36),("James","John","JamesJohn@gmail.com",29)]


conn = sqlite3.connect('customers.db')
c = conn.cursor()
'''Execute many can add iterables into database table'''
c.executemany('''INSERT INTO customers VALUES (?,?,?,?) ''',manyCustomer)
conn.commit()
c.close()
conn.close()

'''QUERY DATABASE'''

conn = sqlite3.connect('customers.db')
c = conn.cursor()

'''We first we want to query the whole database using SELECT'''
c.execute('SELECT * FROM customers') # Selects all rows and columns in table in database
c.fetchone()
c.fetchmany(3) # Fetches top 3 rows
print(c.fetchall())

'''A Primary Key - is used in most common database which allows each row each table in the database a unique number. Also known as ROW ID'''

conn = sqlite3.connect('customers.db')
c = conn.cursor()

c.execute('SELECT rowid,* FROM customers') # select rowid and all rows and columns from customers table
'''Returns row id within each tuple item within list'''

print('----------')
print(c.fetchall())

'''Searching for more specific data from tables in database'''

c.execute('SELECT * FROM customers WHERE age<45 AND First_Name == "Jack"')
print('00000000000000')
print(c.fetchall())

'''Signifies every row in table in database will be returened when it has a first name starting with "J"'''
c.execute('SELECT * FROM customers WHERE First_Name LIKE "J%"')


'''Selects rows of data of individual users who have a last name that starts "La"'''
c.execute('SELECT * FROM customers WHERE last_name LIKE "La%"')
print(c.fetchall())

'''Updating records'''

c.execute('''UPDATE customers SET last_name = "Mohammed" WHERE First_Name = "Lane"''') 
'''Updates Customers by setting last_name to mohammed who have first_Name Lane'''
conn.commit() # Commits/saves this update

print('')
print('')

c.execute('SELECT * FROM customers ')
print(c.fetchall())

'''However, the above update is not the most efficent way

The best way to update individual rows of user data is to use the unique rowid or primary keys
'''
c.execute('SELECT rowid,* FROM customers')
print('SPACE')
print(c.fetchone())

'''Now we can update using the rowid '''

c.execute('UPDATE customers SET last_name = "ELER" WHERE rowid = 1') # Syntax required to update
conn.commit() # commit/save change to table in database

'''Delete a record'''

c.execute('DELETE FROM customers WHERE rowid = 6 ') # Permeanetly deletes row of user information
conn.commit()

'''Ordering database'''

c.execute('SELECT rowid,* FROM customers ORDER BY rowid DESC')
conn.commit()

print(c.fetchall())

print('Printed')
c.execute('SELECT rowid,* FROM customers ORDER BY First_Name Desc')
print(c.fetchall())

'''AND/OR conditional to where clause'''


'''Limiting results

In reality databases will include thousands/millions of user data which will be needed to cut into shorter chunks to be easier to go through.

This can be done using the LIMIT which requires an interger for the number of row of user information 

LIMIT 4 -> will return 4 rows of user information

Note: LIMIT should always be specified on the end of an EXECUTE string
'''

'''Will return rowid and all columns which is limited to 3 rows'''
c.execute('SELECT rowid,* FROM customers LIMIT 3')
print(c.fetchall())


'''Drop a table - Deleting a table from a database

This is a permeanent move
'''

c.execute('DROP TABLE customers') # Table dropped from database
conn.commit() # commit/save the change

'''This can now be checked by checking the existence in the database - it should return no such table: customers'''

c.execute('SELECT rowid,* FROM customers')
print('DELETED')
print(c.fetchall())


