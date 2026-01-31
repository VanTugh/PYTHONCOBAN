# class Diem:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def nhap(self):
#         self.x = float(input("Nhap hoanh do x: "))
#         self.y = float(input("Nhap tung do y: "))

#     def hien_thi(self):
#         print(f"Diem({self.x}, {self.y})")
# class DoanThang:
#     def __init__(self, diem_a , diem_b):
#         self.diem_a = diem_a
#         self.diem_b = diem_b
#     def tinh_do_dai(self):
#         return ((self.diem_b.x - self.diem_a.x) ** 2 + (self.diem_b.y - self.diem_a.y) ** 2) ** 0.5
# class TamGiac:
#     def __init__(self, doan_ab, doan_bc, doan_ca , tam_diem):   
#         self.doan_ab = doan_ab
#         self.doan_bc = doan_bc
#         self.doan_ca = doan_ca
#         self.tam_diem = tam_diem
#     def dien_tich(self):
#         a = self.doan_ab.tinh_do_dai()
#         b = self.doan_bc.tinh_do_dai()
#         c = self.doan_ca.tinh_do_dai()
#         if a + b <= c or a + c <= b or b + c <= a:
#             print("Ba diem khong tao thanh tam giac.")
#             return 0
#         else:
#             p = (a + b + c) / 2
#             return (p * (p - a) * (p - b) * (p - c)) ** 0.5
# def main():
#     print("Nhap diem A:")
#     diem_a = Diem()
#     diem_a.nhap()
#     print("Nhap diem B:")
#     diem_b = Diem()
#     diem_b.nhap()
#     print("Nhap diem C:")
#     diem_c = Diem()
#     diem_c.nhap()

#     doan_ab = DoanThang(diem_a, diem_b)
#     doan_bc = DoanThang(diem_b, diem_c)
#     doan_ca = DoanThang(diem_c, diem_a)

#     tam_diem = (diem_a, diem_b, diem_c)
#     tam_giac = TamGiac(doan_ab, doan_bc, doan_ca, tam_diem)

#     print("Dien tich tam giac ABC:", tam_giac.dien_tich())
# if __name__ == "__main__":
#     main()
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def nhap(self):
        self.x = float(input("Nhap hoanh do x: "))
        self.y = float(input("Nhap tung do y: "))

    def hien_thi(self):
        print(f"Diem({self.x}, {self.y})")
class DoanThang:
    def __init__(self, diem_a , diem_b):
        self.diem_a = diem_a
        self.diem_b = diem_b
    def tinh_do_dai(self):
        return ((self.diem_b.x - self.diem_a.x) ** 2 + (self.diem_b.y - self.diem_a.y) ** 2) ** 0.5
class TamGiac:
    def __init__(self, doan_ab, doan_bc, doan_ca , tam_diem):   
        self.doan_ab = doan_ab
        self.doan_bc = doan_bc
        self.doan_ca = doan_ca
        self.tam_diem = tam_diem
    def dien_tich(self):
        a = self.doan_ab.tinh_do_dai()
        b = self.doan_bc.tinh_do_dai()
        c = self.doan_ca.tinh_do_dai()
        if a + b <= c or a + c <= b or b + c <= a:
            print("Ba diem khong tao thanh tam giac.")
            return 0
        else:
            p = (a + b + c) / 2
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5
def main():
    print("Nhap diem A:")
    diem_a = Diem()
    diem_a.nhap()
    print("Nhap diem B:")
    diem_b = Diem()
    diem_b.nhap()
    print("Nhap diem C:")
    diem_c = Diem()
    diem_c.nhap()

    doan_ab = DoanThang(diem_a, diem_b)
    doan_bc = DoanThang(diem_b, diem_c)
    doan_ca = DoanThang(diem_c, diem_a)

    tam_diem = (diem_a, diem_b, diem_c)
    tam_giac = TamGiac(doan_ab, doan_bc, doan_ca, tam_diem)

    print("Dien tich tam giac ABC:", tam_giac.dien_tich())
if __name__ == "__main__":
    main()
