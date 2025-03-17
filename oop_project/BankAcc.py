class BalanceException(Exception): 
    pass
  
class BankAcc:
    def __init__(self, amount, accName):
     self.Balance = amount
     self.accName = accName
     print(f"\n accName '{self.accName}' created. \n balance = $'{self.Balance}'")
    def getBalance(self):
     print(f" accName '{self.accName}' balance = $'{self.Balance}'")
     
    def deposit(self, depamount):
        self.Balance+=depamount
        print("\n deposit complete sir.")
        self.getBalance()
        
    def ViableTransaction(self, money):
        if self.Balance>=money:
            return
        else:
            raise BalanceException(f"\nmoney isn't enough sir:( u onley have '{self.Balance}'")
        
    def withdraw(self,money):
        try:
            self.ViableTransaction(money)
            self.Balance-=money
            print("withdraw complete sir<3")
            self.getBalance()
            
        except BalanceException as error:
            print(f"withdraw went wrong {error}")
            
    def transfer(self, money, accName):
        try:
            print("\n ****transfer in process****")
            self.ViableTransaction(money)
            self.withdraw(money)
            accName.deposit(money)
            print("\n transfer complete sir<3")
            
        except BalanceException as error:
            print(f"transfer went wrong {error}")

class Commisions(BankAcc):
    def deposit(self, depamount):
        self.Balance+=(depamount*1.5)
        print("\ncommision added<3")
        self.getBalance()
        
class SavingAcc(Commisions):
    def __init__(self, amount, accName):
        super().__init__(amount,accName)
        self.fee = 5
        
    def withdraw(self,money):
        try:
            self.ViableTransaction(money+self.fee)
            self.Balance-=(money+self.fee)
            print("withdraw complete sir<3")
            self.getBalance()
            
        except BalanceException as error:
            print(f"withdraw went wrong {error}")

        
