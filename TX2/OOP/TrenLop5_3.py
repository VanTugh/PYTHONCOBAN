class NhanVien:
    def __init__(self, ma_nv, ten_nv, luong_cb):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv
        self.luong_cb = luong_cb


    def hien_thi_thong_tin(self):
        print(f"Mã NV: {self.ma_nv}, Tên NV: {self.ten_nv}, Lương CB: {self.luong_cb}")
class NhanVienBanHang(NhanVien):
    def __init__(self, ma_nv, ten_nv, luong_cb,danh_so):
        super().__init__(ma_nv, ten_nv, luong_cb)
        self.danh_so = danh_so
    def tinh_luong(self):
        return self.luong_cb + 0.05 * self.danh_so
class NhanVienQuanLy(NhanVien):
    def __init__(self, ma_nv, ten_nv, luong_cb,so_ngay_cong):
        super().__init__(ma_nv, ten_nv, luong_cb)
        self.so_ngay_cong = so_ngay_cong
    def tinh_luong(self):
        return self.luong_cb + 50 * self.so_ngay_cong
def main():
    nv_bh = NhanVienBanHang("NV001", "Nguyen Van A", 5000000, 20000000)
    nv_ql = NhanVienQuanLy("NV002", "Tran Thi B", 7000000, 22)

    nv_bh.hien_thi_thong_tin()
    print(f"Lương NV Bán Hàng: {nv_bh.tinh_luong()}")

    nv_ql.hien_thi_thong_tin()
    print(f"Lương NV Quản Lý: {nv_ql.tinh_luong()}")
if __name__ == "__main__":
    main()
        