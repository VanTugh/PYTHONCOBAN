from Account import Account

class SavingAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Da gui {amount}")
        else:
            print("So tien gui phai > 0")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Da rut {amount}")
            return amount
        else:
            print("So du khong du")
            return 0

    def get_balance(self):
        return self.balance
