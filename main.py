from checking import checking
from savings import savings

# Main Method
if __name__ == '__main__':
    """daveBank = BankAccount("Dave",3000.00,300.00)
    daveBank.deposit(500)
    daveBank.withdraw(500.00)
    daveBank.withdraw(5000.00)
    daveBank.print_customer_information()"""

    #Checking Account Test
    daveChecking = checking("Dave", 3000.00, 300.00, "8749326472", "7432947320")
    daveChecking.deposit(500)
    daveChecking.withdraw(100)
    daveChecking.withdraw(5600)
    daveChecking.print_customer_information()

    #Savings Account Test
    daveSavings = savings("Dave", 3000.00, 300.00, 3.5)  # 3.5% annual interest rate
    daveSavings.deposit(1000) 
    daveSavings.withdraw(500)  
    daveSavings.apply_interest()  
    daveSavings.print_customer_information()  
    

