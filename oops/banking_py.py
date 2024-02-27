from random import randint
 
 
class Banking:
    def __init__(self) -> None:
        self.holder_name: str = input("Enter holder name = ").title()
        self.account_type: str = input("Enter savings/current/other = ").title()
        self.account_number: int = randint(100000, 999999)
        self.balance: float = 0.0
 
    def getBalance(self) -> float:
        return self.balance
 
    def displayDetails(self) -> None:
        print("\n------DETAILS------")
        print(f"Account number = {self.account_number}")
        print(f"Holder name = {self.holder_name}")
        print(f"Account Type name = {self.account_type}")
        print(f"Balance = {self.balance}\n")
 
    def withdraw(self, amt) -> None:
        if amt > self.balance:
            print("Insufficient balance in your bank")
            return
 
        self.balance = self.balance - amt
        print(f"Remaining balance = {self.balance}")
 
    def deposit(self, amt: float) -> None:
        self.balance += amt
        print(f"Remaining balance = {self.balance}")
 
 
accounts = []
 
while True:
    print(
        """\n1. Add Account
2. Display all accounts
3. Search account
4. Get balance
5. Deposit 
6. Withdraw
7. Exit"""
    )
    choice = int(input("Enter your choice = "))
    if choice == 1:
        obj = Banking()
        accounts.append(obj)
        print("Account created")
    elif choice == 2:
        print(accounts)
        if len(accounts) == 0:
            print("No accounts aviable")
        for bank in accounts:
            bank.displayDetails()
    elif choice == 7:
        break
    else:
        print("Invalid Choice")