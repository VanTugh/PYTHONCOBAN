from typing import Protocol, List

# --- 1. ĐỊNH NGHĨA KHUÔN MẪU (PROTOCOL) ---
# Bất kỳ class nào có đủ 2 hàm này sẽ được coi là "UngVien" hợp lệ.
class UngVienKhenThuong(Protocol):
    def xet_khen_thuong(self) -> bool:
        ...

    def lay_thong_tin(self) -> str:
        ...

# --- 2. CÁC CLASS CỤ THỂ (KHÔNG CẦN KẾ THỪA PROTOCOL) ---

class SinhVien:
    def __init__(self, ten, gpa):
        self.ten = ten
        self.gpa = float(gpa)
        self.bo_phan = "Sinh viên"

    # Duck Typing: Có hàm xet_khen_thuong
    def xet_khen_thuong(self) -> bool:
        return self.gpa > 3.2

    # Duck Typing: Có hàm lay_thong_tin
    def lay_thong_tin(self) -> str:
        return f"{self.ten} - {self.bo_phan} (GPA: {self.gpa})"


class GiangVien:
    def __init__(self, ten, so_cong_trinh):
        self.ten = ten
        self.so_cong_trinh = int(so_cong_trinh)
        self.bo_phan = "Giảng viên"

    def xet_khen_thuong(self) -> bool:
        return self.so_cong_trinh >= 2

    def lay_thong_tin(self) -> str:
        return f"{self.ten} - {self.bo_phan} (Bài báo: {self.so_cong_trinh})"


class QuanLy:
    def __init__(self, ten, hoan_thanh_tot):
        self.ten = ten
        self.hoan_thanh_tot = hoan_thanh_tot # True/False
        self.bo_phan = "Quản lý"

    def xet_khen_thuong(self) -> bool:
        return self.hoan_thanh_tot

    def lay_thong_tin(self) -> str:
        trang_thai = "Tốt" if self.hoan_thanh_tot else "Chưa tốt"
        return f"{self.ten} - {self.bo_phan} (Đánh giá: {trang_thai})"


# --- 3. CHƯƠNG TRÌNH XỬ LÝ ---

# Hàm này chấp nhận list các đối tượng tuân thủ Protocol "UngVienKhenThuong"
def thong_bao_khen_thuong(danh_sach: List[UngVienKhenThuong]):
    print("=== DANH SÁCH ĐƯỢC KHEN THƯỞNG ===")
    count = 0
    for nguoi in danh_sach:
        # Nhờ Protocol, IDE sẽ biết chắc chắn biến 'nguoi' có hàm xet_khen_thuong
        if nguoi.xet_khen_thuong():
            print(f" {nguoi.lay_thong_tin()}")
            count += 1
            
    if count == 0:
        print("Không có ai đủ điều kiện.")

# --- 4. CHẠY THỬ ---
def main():
    # Tạo danh sách hỗn hợp
    ds_nhan_su = [
        SinhVien("Nguyen Van A", 3.5),      # Đạt (>3.2)
        SinhVien("Le Thi B", 3.0),          # Trượt
        GiangVien("Thay C", 5),             # Đạt (>=2)
        GiangVien("Co D", 1),               # Trượt
        QuanLy("Sep E", True),              # Đạt
        QuanLy("Sep F", False)              # Trượt
    ]

    thong_bao_khen_thuong(ds_nhan_su)

if __name__ == "__main__":
    main()