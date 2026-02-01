from abc import ABC, abstractmethod
class NCC:
    def __init__(self,maNCC, nameNCC,address):
        self.maNCC = maNCC
        self.name = nameNCC
        self.address = address
class Hang(ABC):
    def __init__(self, nameHang, price, quantity):
        self.nameHang = nameHang
        self.price = price
        self.quantity = quantity
    @abstractmethod
    def thue(self):
        pass
    def thanhTien(self):
        return self.price * self.quantity * (1 - self.thue())
class TV(Hang):
    def thue(self):
        return 0.1 
class Quat(Hang):
    def thue(self):
        return 0.05
class Mobi(Hang):
    def thue(self):
        return 0.2
class Phieu():
    def __init__(self, maPhieu , ngayLap):
        self.maPhieu = maPhieu
        self.ngayLap = ngayLap
        self.dsHang = []
    def nhap_hang(self):
        n = int(input("Nhap so luong hang: "))
        for i in range(n):
            loai = input("Nhap loai hang (TV/Quat/Mobi): ")
            name = input("Nhap ten hang: ")
            price = float(input("Nhap don gia: "))
            quantity = int(input("Nhap so luong: "))
            if loai == "TV":
                hang = TV(name, price, quantity)
            elif loai == "Quat":
                hang = Quat(name, price, quantity)
            elif loai == "Mobi":
                hang = Mobi(name, price, quantity)
            else:
                print("Loai hang khong hop le!")
                continue
            self.dsHang.append(hang)
    def themHang(self, hang):
        return self.dsHang.append(hang)
    def tinhTongTien(self):
        tong = 0 
        for hang in self.dsHang:
            tong += hang.thanhTien()
        return tong
    staticmethod
    def inPhieu(self, ncc):
        print("=" * 65)
        print("PHIẾU NHẬP HÀNG".center(65))
        print("=" * 65)

        print(f"Mã phiếu: {self.maPhieu:<15} Ngày lập: {self.ngayLap}")
        print(f"Mã NCC:   {ncc.maNCC:<15} Tên NCC: {ncc.name}")
        print(f"Địa chỉ:  {ncc.address}")
        print("-" * 65)

    # Header bảng
        print(f"{'Tên hàng':<25}{'Đơn giá':>10}{'Số lượng':>10}{'Thành tiền':>15}")
        print("-" * 65)

    # Nội dung bảng
        for hang in self.dsHang:
            thanh_tien = hang.thanhTien()
            print(f"{hang.nameHang:<25}{hang.price:>10.2f}{hang.quantity:>10}{thanh_tien:>15.2f}")

        print("-" * 65)
        print(f"{'Cộng thành tiền':<35}{self.tinhTongTien():>15.2f}")
        print("=" * 65)

    def thanh_tien_max(self):
        max_hang = max(self.dsHang, key = lambda hang : hang.thanhTien())
        return max_hang 
    def sapxep(self):
        return self.dsHang.sort(key= lambda hang : hang.quantity, reverse= True)
def main():
    ncc = NCC("NCC001", "Cty ABC", "123 Duong XYZ")
    phieu = Phieu("PH001", "01/01/2024")
    tv = TV("Tivi Samsung", 1000, 2)
    quat = Quat("Quat Panasonic", 200, 5)
    mobi = Mobi("Dien thoai iPhone", 1500, 1)
    phieu.themHang(tv)
    phieu.themHang(quat)
    phieu.themHang(mobi)
    phieu.inPhieu(ncc)
    max_hang = phieu.thanh_tien_max()
    print(max_hang.nameHang)
    phieu.sapxep()
    for hang in phieu.dsHang:
        print(hang.nameHang +" : ", hang.quantity)
if __name__ == "__main__":
    main()