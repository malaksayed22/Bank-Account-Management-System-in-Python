from BankAcc import*
malak = BankAcc(1000,"malak")
menna = BankAcc(2000, "menna")
mrmr = Commisions(500,"mrmr")
doaa = SavingAcc(3000,"doaa")
malak.getBalance()
menna.getBalance()

malak.deposit(500)
menna.deposit(150)

malak.withdraw(1000)
menna.withdraw(400)

malak.transfer(500,menna)

mrmr.deposit(200)
mrmr.transfer(900,malak)

doaa.deposit(100)
doaa.transfer(100,malak)