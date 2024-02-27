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
 
 
b1 = Banking()
b1.deposit(1000)
 
b2 = Banking()
b2.deposit(2000)
 
transfer_amt = int(input("Enter transfer amount = "))
b1.withdraw(transfer_amt)
b2.deposit(transfer_amt)
 