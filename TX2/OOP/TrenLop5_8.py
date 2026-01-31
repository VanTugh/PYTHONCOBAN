class SoPhuc:
    def __init__(self, thuc ,ao):
        self.thuc = thuc
        self.ao = ao
    def __str__(self):
        return f"{self.thuc} + {self.ao}i"
    def __pow__(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)
    def __floordiv__(self, other):
        return SoPhuc(self.thuc - other.thuc, self.ao - other.ao)
def main():
    sp1 = SoPhuc(2, 3)
    sp2 = SoPhuc(4, 5)

    sp_cong = sp1 ** sp2
    sp_tru = sp1 // sp2

    print(f"Cong: {sp_cong}")
    print(f"Tru: {sp_tru}")
if __name__ == "__main__":
    main()