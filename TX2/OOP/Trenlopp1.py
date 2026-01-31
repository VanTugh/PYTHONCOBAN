class Nguoi:
    def __init__(self, ho_ten, tuoi, can_nang, chieu_cao    ):
        self.ho_ten = ho_ten
        self.tuoi = int(tuoi)
        self.can_nang = float(can_nang)
        self.chieu_cao = float(chieu_cao)
    def __str__(self):
        return f"Họ tên: {self.ho_ten}, Tuổi: {self.tuoi}, Cân nặng: {self.can_nang} kg, Chiều cao: {self.chieu_cao} m"
    def chuc_mung_sinh_nhat(self):
        self.tuoi += 1
        print(f"Chúc mừng sinh nhật {self.ho_ten}, bạn đã tròn {self.tuoi} tuổi!")
def bai5_1_main():
    nguoi1 = Nguoi("Nguyễn Văn A", 25, 70, 1.75)
    print(nguoi1)
    nguoi1.chuc_mung_sinh_nhat()
    print(nguoi1)
if __name__ == "__main__":
    bai5_1_main()