class SanPham:
    def __init__(self, ma_sp, ten_sp, gia_ban):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.gia_ban = gia_ban

    def __str__(self):
        return f"Ma SP: {self.ma_sp} | Ten SP: {self.ten_sp} | Gia ban: {self.gia_ban}"
class DonHang:
    def __init__(self, ma_dh, ngay_lap):
        self.ma_dh = ma_dh
        self.ngay_lap = ngay_lap
        self.ds_san_pham = []
    def nhap_san_pham(self):
        n = int(input("Nhap so luong san pham can them: "))
        for _ in range(n):
            # ma_sp = input("Nhap ma san pham: ")
            # ten_sp = input("Nhap ten san pham: ")
            # gia_ban = float(input("Nhap gia ban san pham: "))
            # san_pham = SanPham(ma_sp, ten_sp, gia_ban)
            # self.them_san_pham(san_pham)
            ma_sp , ten_sp , gia_ban = input("nhap :").strip().split()
            self.them_san_pham(SanPham(ma_sp,ten_sp,float(gia_ban)))
    def them_san_pham(self, san_pham):
        if not any(sp.ma_sp == san_pham.ma_sp for sp in self.ds_san_pham):
            self.ds_san_pham.append(san_pham)
        else:
            print(f"San pham voi ma {san_pham.ma_sp} da ton tai trong don hang.")
    def xoa_san_pham(self, ma_sp):
        if any(sp.ma_sp == ma_sp for sp in self.ds_san_pham):
            self.ds_san_pham = [sp for sp in self.ds_san_pham if sp.ma_sp != ma_sp]
        else:
            print(f"San pham voi ma {ma_sp} khong ton tai trong don hang.")
    def sua_sp_gia(self, ma_sp, gia_moi):
        for sp in self.ds_san_pham:
            if sp.ma_sp == ma_sp:
                sp.gia_ban = gia_moi
                return
        print(f"San pham voi ma {ma_sp} khong ton tai trong don hang.")
    def sap(self):
        self.ds_san_pham.sort(key= lambda x : x.gia_ban, reverse=True)
    def tinh_tong_tien(self):
        return sum(sp.gia_ban for sp in self.ds_san_pham)
    def __add__(self, other):
        new_dh = DonHang(self.ma_dh + "&" + other.ma_dh, self.ngay_lap)
        new_dh.ds_san_pham = self.ds_san_pham + other.ds_san_pham
        return new_dh
    def __str__(self):
        san_pham_str = '\n'.join(str(sp) for sp in self.ds_san_pham)
        return f"Ma DH: {self.ma_dh} | Ngay lap: {self.ngay_lap}\nDanh sach san pham:\n{san_pham_str}\nTong tien: {self.tinh_tong_tien()}"
class DonHangOnline(DonHang):
    def __init__(self, ma_dh, ngay_lap, dia_chi_giao_hang, cuoc_phi):
        super().__init__(ma_dh, ngay_lap)
        self.dia_chi_giao_hang = dia_chi_giao_hang
        self.cuoc_phi = cuoc_phi
    def tinh_tong_tien(self):
        return super().tinh_tong_tien() + self.cuoc_phi
def luufile(don_hang, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(don_hang))
def main():
    sp1 = SanPham("SP001", "San Pham 1", 100000)
    sp2 = SanPham("SP002", "San Pham 2", 200000)
    dh1 = DonHang("DH001", "2024-06-01")
    # dh1.them_san_pham(sp1)  
    # dh1.them_san_pham(sp2)
    # print(dh1)
    dh1.nhap_san_pham()
    print(dh1)
    dh2 = DonHangOnline("DH002", "2024-06-02", "123 Duong ABC", 50000)
    dh2.them_san_pham(sp2)
    print(dh2)
    dh_combined = dh1 + dh2
    print(dh_combined)

    #
    sp_new = SanPham("SP003", "San Pham 3", 150000)
    dh1.them_san_pham(sp_new)
    print("them san pham : \n",dh1)

    dh1.sua_sp_gia("SP004", 120000)
    print("sua gia san pham : \n",dh1)

    dh1.xoa_san_pham("SP004")
    print("xoa san pham : \n",dh1)

    dh1.sap()
    print("sap giam dan theo gia : \n", dh1)

    luufile(dh1, "don_hang.txt")
if __name__ == "__main__":
    main()