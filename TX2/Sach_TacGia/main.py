from datetime import date
class TacGia:
    def __init__(self, ten, quocTich):
        self.ten = ten
        self.quoctich = quocTich
    def __str__(self):
        return f"ten : {self.ten} | quoc tich : {self.quoctich}"
class Sach:
    def __init__(self , ma_sach , ten_sach, namXB, tac_gia):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.namXB = int(namXB)
        self.tac_gia = tac_gia
    def __str__(self):
        return f"ma sach : {self.ma_sach} | ten : {self.ten_sach} | nam xuat ban : {self.namXB} | tac gia {self.tac_gia}"
    def get_tuoi_sach(self):
        return date.today().year - self.namXB
    def __add__(self, other):
        return f"Tong hop : {self.ten_sach} & {other.ten_sach}"
class GiaoTrinh(Sach):
    def __init__(self, ma_sach, ten_sach, namXB, tac_gia, mon_hoc):
        super().__init__(ma_sach, ten_sach, namXB, tac_gia)
        self.mon_hoc = mon_hoc
    def __str__(self):
        return super().__str__() + f" | mon hoc : {self.mon_hoc} | tuoi sach : {self.get_tuoi_sach()}"
class ThamKhao(Sach):
    def __init__(self, ma_sach, ten_sach, namXB, tac_gia, linh_vuc):
        super().__init__(ma_sach, ten_sach, namXB, tac_gia)
        self.linh_vuc = linh_vuc
    def __str__(self):
        return super().__str__() + f" | linh vuc : {self.linh_vuc} | tuoi sach : {self.get_tuoi_sach()}"
def main():
    tg1 = TacGia("Nguyen Tung", "Ha Noi")
    tg2 = TacGia("Huu Ly","Dong Anh")
    gt1 = GiaoTrinh("001","Cho toi qua cam",2012,tg1,"Cam xuc khoa hoc")
    tk1 = ThamKhao("002","Se ra sao",2021,tg2,"Khoa hoc")
    print(gt1)
    print(tk1)
    new_sach = gt1 + tk1
    print(new_sach)
if __name__ =="__main__":
    main()