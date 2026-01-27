class TamThucBac2():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f" = {self.a}x*x + {self.b}x + {self.c}"
    def __neg__(self):
        return TamThucBac2(-self.a, -self.b, -self.c)
    def __add__(self, other):
        return TamThucBac2(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c
        )
def main():
    t1 = TamThucBac2(1, 2, 3)
    t2 = TamThucBac2(4, 5, 6)
    print("Tam thuc 1 : ", t1)
    print("Tam thuc 2 : ", t2)
    t3 = -t1
    print("Doi dau tam thuc 1 : ", t3)
    t4 = t1 + t2
    print("Tong 2 tam thuc : ", t4)
if __name__ == "__main__":
    main()