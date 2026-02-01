class HCN:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    def display(self):
        print(f"HCN có chiều dài: {self.length}, chiều rộng: {self.width}")
        print(f"Diện tích: {self.area()}")
        print(f"Chu vi: {self.perimeter()}")
if __name__ == "__main__":
    hcn1 = HCN(5, 3)
    hcn1.display()

    hcn2 = HCN(10, 4)
    hcn2.display()