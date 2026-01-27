class Person:
    def __init__(self, ten, date, que):
        self.ten = ten
        self.date = date
        self.que = que
    def __str__(self):
        return f"| Ten : {self.ten} | Ngay Sinh : {self.date} | Que quan : {self.que} |"
