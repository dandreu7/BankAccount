from BankAccount import BankAccount

class savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._interest_rate = interest_rate
        
        
    def apply_interest(self):
        interest = self.current_balance * (self._interest_rate / 100)
        self.current_balance += interest
        print(f"Interest applied at {self._interest_rate}%: {interest}")
        print(f"New Balance after interest: {self.current_balance}\n")
        return self.current_balance



