class AtmCard:
    def __init__(self):
        self.current_balance = 2000

    def withdraw(self, amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            return self.current_balance
        return False

    def deposit(self, amount):
        self.current_balance += amount
        return self.current_balance

class CreditCard:
    def __init__(self):
        self.maximum_allowance = 5000

    def doShopping(self, amount):
        if self.maximum_allowance >= amount:
            self.maximum_allowance -= amount
            return self.maximum_allowance
        return False
    
    # will create problem as this will override the transfer form 
    # def transfer(self, account_number, amount):
    #     if self.maximum_allowance >= amount:
    #         self.maximum_allowance -= amount
    #         return "Transfer to my " + account_number + " which will be RM " + str(self.maximum_allowance)
    #     return False

class DebitCard:
    def __init__(self):
        self.current_balance = 2000
    
    def transfer(self, account_number, amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            return "Transfer to " + account_number + " RM " + str(self.current_balance)
        return False

class BankCard(AtmCard, CreditCard, DebitCard):
    def __init__(self):
        super().__init__() # This calls AtmCard.__init__()
        # AtmCard.__init__(self)    
        CreditCard.__init__(self)
        DebitCard.__init__(self)

myBankCard = BankCard()

print("Amount left: ",myBankCard.withdraw(1000))
print("Amount left: ",myBankCard.deposit(1000))
print(myBankCard.transfer("341-435-456", 230))
print("Allowance left: ",myBankCard.doShopping(599))