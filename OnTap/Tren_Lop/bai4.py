from abc import ABC, abstractmethod

# ===== LỚP CHA (ABSTRACT CLASS) =====
class NhanVien(ABC):
    def __init__(self, ho_ten, ma_nhan_vien):
        self.ho_ten = ho_ten
        self.ma_nhan_vien = ma_nhan_vien

    @abstractmethod
    def tinh_luong(self):
        pass   # Chỉ định nghĩa hợp đồng

    def __eq__(self, other):
        if not isinstance(other, NhanVien):
            return False
        return self.tinh_luong() == other.tinh_luong()


# ===== NHÂN VIÊN VĂN PHÒNG =====
class NVVP(NhanVien):
    def __init__(self, ho_ten, ma_nhan_vien, so_gio_lam, luong_gio):
        super().__init__(ho_ten, ma_nhan_vien)
        self.so_gio_lam = so_gio_lam
        self.luong_gio = luong_gio

    def tinh_luong(self):
        return self.so_gio_lam * self.luong_gio

    def __str__(self):
        return (
            f"NV Văn Phòng | "
            f"Họ tên: {self.ho_ten}, "
            f"Mã NV: {self.ma_nhan_vien}, "
            f"Lương: {self.tinh_luong()}"
        )


# ===== NHÂN VIÊN SẢN XUẤT =====
class NVSX(NhanVien):
    def __init__(self, ho_ten, ma_nhan_vien, so_san_pham, tien_moi_sp):
        super().__init__(ho_ten, ma_nhan_vien)
        self.so_san_pham = so_san_pham
        self.tien_moi_sp = tien_moi_sp

    def tinh_luong(self):
        return self.so_san_pham * self.tien_moi_sp

    def __str__(self):
        return (
            f"NV Sản Xuất | "
            f"Họ tên: {self.ho_ten}, "
            f"Mã NV: {self.ma_nhan_vien}, "
            f"Lương: {self.tinh_luong()}"
        )


# ===== CHƯƠNG TRÌNH CHÍNH =====
if __name__ == "__main__":
    nvvp = NVVP("Nguyễn Văn A", "VP01", 160, 50000)
    nvsx = NVSX("Trần Thị B", "SX01", 400, 20000)

    print(nvvp)
    print(nvsx)

    if nvvp == nvsx:
        print("👉 Hai nhân viên có lương bằng nhau")
    else:
        print("👉 Hai nhân viên có lương KHÔNG bằng nhau")
