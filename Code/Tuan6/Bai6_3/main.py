class BankAccount:
    def __init__(self, account_number,name ,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Nạp tiền thành công! Số dư hiện tại: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Số dư không đủ để rút tiền.")
        else:
            self.balance -= amount
            print(f"Rút tiền thành công! Số dư hiện tại: {self.balance}")
    def bankFee(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print(f"Phí dịch vụ đã được trừ: {fee}. Số dư hiện tại: {self.balance}")
    def display(self):
            print(f"Số tài khoản: {self.account_number}, Tên chủ tài khoản: {self.name}, Số dư: {self.balance}")    
if __name__ == "__main__":
    account = BankAccount("123456789", "Nguyen Van A", 1000)
    account.display()
    account.deposit(500)
    account.withdraw(200)
    account.bankFee()
    account.display()