class Account:
    def get_balance(self):
        pass

class Transaction:
    def execute(self):
        pass

class SavingsAccount(Account):
    def get_balance(self):
        # Logic to retrieve balance for savings account
        print('Your balance is $5')

class CheckingAccount(Account):
    def get_balance(self):
        # Logic to retrieve balance for checking account
        print('Your balance is $25')

class Deposit(Transaction):
    def execute(self):
        # Logic to execute a deposit transaction
        print('Your balance is deposited')

class Withdrawal(Transaction):
    def execute(self):
        # Logic to execute a withdrawal transaction
        print('Withdrawl money for $10')



# In this bank management example:

# 1- Account defines the common behavior for all types of bank accounts, which is getting the account balance.

# 2- Transaction defines the common behavior for all types of transactions, which is executing the transaction.

# 3- SavingsAccount and CheckingAccount implement the Account interface, providing the specific logic to retrieve balances for their respective account types.

# 4- Deposit and Withdrawal implement the Transaction interface, providing the specific logic to execute deposit and withdrawal transactions.

# 5- By separating the behaviors into specific interfaces (Account and Transaction), 
# we ensure that each class only implements the methods that are relevant to its role. 
# This adheres to the Interface Segregation Principle and helps create a more modular 
# and maintainable bank management system.


