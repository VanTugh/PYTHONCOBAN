class PhanSo:
    def __init__(self, tu_so , mau_so):
        if mau_so == 0:
            raise ValueError("Mau so khong duoc bang 0.")
        self.tu_so = int(tu_so)
        self.mau_so = int(mau_so)
    def __add__(self, other):
        tu_so_moi = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau_so_moi = self.mau_so * other.mau_so
        return PhanSo(tu_so_moi, mau_so_moi)
    def __mul__(self, other):
        tu_so_moi = self.tu_so * other.tu_so
        mau_so_moi = self.mau_so * other.mau_so
        return PhanSo(tu_so_moi, mau_so_moi)
    def __eq__(self, other):
        if isinstance(other, PhanSo):
            return self.tu_so * other.mau_so == other.tu_so * self.mau_so
        elif isinstance(other, (int, float)):
            return self.tu_so / self.mau_so == other
        else:
            return NotImplemented
    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"

def main():
    ps1 = PhanSo(1, 2)
    ps2 = PhanSo(3, 4)

    ps_tong = ps1 + ps2
    ps_tich = ps1 * ps2
    ps_bang_nhau = ps1 == ps2

    print(f"Tong: {ps_tong}")
    print(f"Tich: {ps_tich}")
    print(f"Phan so 1 bang phan so 2: {ps_bang_nhau}")
if __name__ == "__main__":
    main()