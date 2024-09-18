from BankAccount import *
# Main Method
if __name__ == '__main__':
    daveBank = BankAccount("Dave",3000.00,300.00)

    daveBank.deposit(500)
    daveBank.withdraw(500.00)

    daveBank.withdraw(5000.00)

    daveBank.print_customer_information()