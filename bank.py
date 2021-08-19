'''Creating a bank script that adds users to a database and updates database when user deposits,withdraws or leaves bank which would result user to be deleted from table '''
import bank_database as bd
import random
class User:
  def __init__(self,balance = 0,first_name = '',last_name = ''):
    '''Every bank account for a user is intialised with the user personal information and balance. A unique 4 digit id is given to each account'''
    self.BANKNAME = 'Barclays.LTD'
    self.id = random.randint(1000,9999)
    self.balance = balance
    self.first = first_name
    self.last = last_name
    self.add() # Added as soon as object is instantiated
    
  def add(self):
    '''Adds user into database'''
    bd.add_user(self.id,self.balance,self.first,self.last)
    
  def get_info(self):
    '''Allows user to get their own information in their personal info inside their account'''
    bd.get_users_info(self.first,self.last)
    
  def deposit(self,amount):
    self.balance+=amount
    bd.update_balance(self.first,self.last,self.balance)
    
  def withdraw(self,amount):
    '''Withdraw an amount from the amount'''
    self.balance-=amount
    bd.update_balance(self.first,self.last,self.balance)
    
  def delete_account(self):
    '''Deletes account from table'''
    bd.delete_user(self.first,self.last)  


class Admin:
  def show_table(self):
    '''Shows table in database'''
    bd.show_table()
    
  def delete_user(self,row_id):
    '''Delete user from table in database in row id'''
    bd.delete_row(row_id)
    
  def clear_all(self):
    '''Clears all rows in table'''
    bd.clear()

# a  = User(2000,'Landon','Katewell')
# a.get_info()
# a.deposit(100)
# a.get_info()
# a.delete_account()

admin = Admin()
# # admin.delete_user(1)
# admin.show_table()
# admin.clear_all()

# user1 = User(2000,'Jake','Murphy')
# user2 = User(1000,'Maxwell','James')
# user3 = User(150,'Powell','Jones')
# user4 = User('230','Kevin','Meldon')
user5 = User(170,'Landon','Bane')
# user5.deposit(400)
# user5.withdraw(500)

admin.show_table()











    
    
    
