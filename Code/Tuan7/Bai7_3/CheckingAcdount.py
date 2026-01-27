from Account import Account

class CheckingAccount(Account):
    def __init__(self, balance, limit):
        super().__init__(balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount <= self.balance + self.limit:
            self.balance -= amount
            print(f"Da rut {amount}")
            return amount
        else:
            print("Vuot qua han muc")
            return 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Da gui {amount}")
        else:
            print("So tien gui phai > 0")

    def get_balance(self):
        return self.balance
