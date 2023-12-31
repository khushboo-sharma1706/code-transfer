"""Q2:Write a Python class BankAccount with attributes like account_number, balance,
date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance."""

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_joining = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited in the account number {self.account_number}")
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} withdrawn from the account number {self.account_number}")
    def check_balance(self):
        print(f"{self.balance} is the current balance of the account {self.account_number}")
        #return self.balance

account1 = BankAccount(1111,50000,"5 Jan 2023", "Khushboo Sharma")
account2 = BankAccount(2222,60000,"5 Feb 2023", "Bittu Sharma")
account3 = BankAccount(3333,70000,"5 Mar 2023", "Manthan Sharma")

account1.deposit(10000)
account2.deposit(10000)
account3.deposit(10000)

account1.withdraw(5000)
account2.withdraw(5000)
account3.withdraw(5000)

account1.check_balance()
account2.check_balance()
account3.check_balance()
