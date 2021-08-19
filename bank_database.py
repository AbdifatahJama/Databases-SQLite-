'''Bank database module'''

import sqlite3
from datetime import datetime
import random

def create_table_in_database():
  conn = sqlite3.connect('bank_database.db') # Creates bank_database connection object
  c = conn.cursor()
  c.execute('''CREATE TABLE 
            OurCustomers (First_Name TEXT,Last_name TEXT,BANK_ID INTEGER, Current_Balance INTEGER,Account_creation_date TEXT)''') # Creates table called "OurCustomers"
  conn.commit()
  conn.close()
  
  
def add_user(bank_id,balance = 0,first_name = '',last_name = ''):
  '''Adds user into table but will reject accounts with first and last names that are already witin the database'''
  date_now = datetime.now()
  date_now = datetime.strftime(date_now,'%d-%m-%Y')
  conn = sqlite3.connect('bank_database.db') # Connect to database
  c = conn.cursor() # Create cursor
  print(type(c.fetchall()))
  c.execute('SELECT First_Name,Last_name FROM OurCustomers') # Select first and last name
  firstNames = [row[0] for row in c.fetchall()]
  c.execute('SELECT First_Name,Last_name FROM OurCustomers') # Queries database selects first and last name
  lastNames = [last for first,last in c.fetchall()] # Iterates through first and last names and last name appended into lastNames list
  if (first_name in firstNames) and (last_name in lastNames):
    '''IF block triggered first name and last name of user already in list'''
    print('User already in database')
    
  else:
    '''Triggered when a unique name not in database table in instaintated'''
    c.execute('''INSERT INTO OurCustomers VALUES(?,?,?,?,?)''',[first_name,last_name,bank_id,balance,date_now])
    conn.commit()
    conn.close()


def show_table():
  conn = sqlite3.connect('bank_database.db')
  c = conn.cursor()
  c.execute('''SELECT rowid,* FROM OurCustomers''')
  print(c.fetchall())
  conn.close()

def delete_row(row_number):
  '''Deletes row based on row number'''
  conn = sqlite3.connect('bank_database.db')
  c = conn.cursor()
  c.execute('DELETE FROM OurCustomers where rowid =?',(row_number,))
  conn.commit()
  conn.close()
  
def get_users_info(first_name = '',last_name = ''):
  conn = sqlite3.connect('bank_database.db')
  c = conn.cursor()
  c.execute('''SELECT * FROM OurCustomers WHERE First_Name = ? AND Last_name = ? ''',(first_name,last_name))
  for first,last,id,balance,creation_date in c.fetchall():
    print('Name:',first + ' ' + last)
    print('Balance:',balance)
    print('Account Creation Date:',creation_date)
  conn.commit()
  conn.close()
  
def update_balance(first_name,last_name,balance):
  conn = sqlite3.connect('bank_database.db')
  c = conn.cursor()
  c.execute('''UPDATE OurCustomers SET Current_Balance = ? WHERE First_Name = ? AND Last_name = ? ''',(balance,first_name,last_name))
  conn.commit()
  conn.close()
  print('Balance updated')
  
def delete_user(first = '',last = ''):
  '''Deletes user from table based from the first and last name'''
  conn = sqlite3.connect('bank_database.db')
  c = conn.cursor()
  c.execute('''DELETE FROM OurCustomers WHERE First_Name = ? AND Last_name = ? ''',(first,last))
  conn.commit()
  conn.close()
  
def clear():
  '''Clears table completely'''
  conn = sqlite3.connect('bank_database.db')
  c = conn.cursor()
  c.execute('''DELETE FROM OurCustomers''') # DELETES ALL ROWS IN TABLE 
  conn.commit()
  conn.close()
  print('Database cleared')


  
  
  
  
  
  
  
  



