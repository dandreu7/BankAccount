from checking import *
from savings import *
class BankAccount:
    # Class attribute
    title = "Super Bank"

    # Instance attributes
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # Methods
    def deposit(self, amount):
        self.current_balance += amount
        print (f"New Balance after deposit: {self.current_balance}")
        return self.current_balance
    def withdraw(self, amount):
        if (self.current_balance - amount) > self.minimum_balance:
            self.current_balance -= amount
            print( f"New Balance after withdraw: {self.current_balance}")
            return self.current_balance
        else:
            print ("Amount you are trying to withdraw will exceed minimum balance")
            return
    def print_customer_information(self):
        print (f"Welcome to {self.title}\n"
                f"Name: {self.customer_name}\n"
                f"Current Balance: {self.current_balance}\n")
        return

# Test the Class
''' daveBank = BankAccount("Dave",3000.00,300.00)

daveBank.deposit(500)
daveBank.withdraw(500.00)

daveBank.withdraw(5000.00)

daveBank.print_customer_information() '''

