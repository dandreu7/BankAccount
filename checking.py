from main import BankAccount

class checking(BankAccount):

    def transferLimit(self, transferAmount):
        transferAmount = float(input("Enter the amount you want to transfer: "))
        if transferAmount <= 5000:
            self.balance -= transferAmount
            return "Transfer successful. Your new balance is: " + str(self.balance)
        else:
            return "Transfer limit exceeded"