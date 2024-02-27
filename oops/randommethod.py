from random import randint
from typing import List
 
 
class Banking:
    def __init__(self, holder_name: str, account_type: str) -> None:
        self.holder_name: str = holder_name.title()
        self.account_type: str = account_type.title()
        self.account_number: int = randint(100000, 999999)
        self.balance: float = 0.0
 
    def getBalance(self) -> float:
        return self.balance
 
    def displayDetails(self) -> None:
        """
        Display all the details about the bnking application
        """
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
 
 
obj = Banking("Anirudh", "Savings")
obj.displayDetails()
print(obj.displayDetails.__doc__)