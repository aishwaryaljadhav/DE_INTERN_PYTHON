class Account:
    def __init__(self, bal, acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print(f"Amount debited: {amount}")
        print(f"Available balance: {self.get_balance()}")
    def credit(self,amount):
        self.balance+=amount
        print(f"Amount credited: {amount}")
        print(f"Available balance: {self.get_balance()}")
    def get_balance(self):
        return self.balance
a1= Account(10000, 1234567890)
a1.debit(2000)
a1.credit(5000)