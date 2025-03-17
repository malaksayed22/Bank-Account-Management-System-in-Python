# Bank-Account-Management-System-in-Python
A Python-based Bank Account Management System implementing OOP concepts such as inheritance, exceptions, and method overriding

Features:

Basic Bank Account Operations:
*Deposit
*Withdraw
*Transfer funds between accounts
*Custom Exception Handling for insufficient balance

Special Account Types:
*Commission Account: Adds a 50% commission on deposits
*Savings Account: Charges a withdrawal fee

Technologies Used:
*Python 3+
*Object-Oriented Programming (OOP)

Classes & Structure:
1. BankAcc (Base Class):
*Manages balance, deposits, withdrawals, and transfers
*Implements error handling using BalanceException

2. Commisions (Derived from BankAcc):
*Overrides deposit() to add a 50% commission

3. SavingAcc (Derived from Commisions):
*Overrides withdraw() to charge a $5 fee per withdrawal
