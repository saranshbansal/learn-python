class BankAccount:
    def __init__(self, name, balance=0.0):
        print("account created!")
        self.name = name
        self.balance = balance

    def getBalance(self):
        print("Balance checked at " + str(self.balance))
        return self.balance

    def setBalance(self, newBalance):
        print("Balance changed to " + str(newBalance))
        self.balance = newBalance

    def log(self, message):
        myLog = open("Log.txt", "a")
        print(message, file=myLog)
        myLog.close()


myBankAccount = BankAccount("Lisa Turner")
myBankAccount.setBalance(20.0)
print(myBankAccount.getBalance())