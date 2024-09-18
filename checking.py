from BankAccount import BankAccount

class checking(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit = 5000):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.__account_number = account_number  #Private member
        self.__routing_number = routing_number  #Private member
        self._transfer_limit = transfer_limit   #Transfer limit

    def withdraw(self, amount):
        if amount > self._transfer_limit:
            print(f"Transfer limit exceeded: You can only transfer up to {self._transfer_limit}.\n")
        else:
            #Call to BankAccount withdraw method
            super().withdraw(amount)

    #Add additional customer info for checking accounts
    def print_customer_information(self):
        super().print_customer_information()
        print(f"Account Number (Checking): {self.__account_number}\n"
              f"Routing Number (Checking): {self.__routing_number}\n"
              f"Transfer Limit: {self._transfer_limit}\n")
