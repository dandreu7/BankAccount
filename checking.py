from main import BankAccount

class checkingAccount(BankAccount):
    def __init__(self, accountNumber, routingNumber):
        self._accountNumber = accountNumber
        self._routingNumber = routingNumber

    def transferLimit(self, transferAmount):
        transferAmount = float(input("Enter the amount you want to transfer: "))
        if transferAmount <= 5000:
            self.balance -= transferAmount
            return "Transfer successful. Your new balance is: " + str(self.balance)
        else:
            return "Transfer limit exceeded"