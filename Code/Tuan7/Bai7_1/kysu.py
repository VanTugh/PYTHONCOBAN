from person import Person

class KySu(Person):
    def __init__(self, ten, date, que, nganh_hoc, nam_tot_nghiep):
        super().__init__(ten, date, que)
        self.nganh_hoc = nganh_hoc
        self.nam_tot_nghiep = nam_tot_nghiep
        self.DS =[]

    def __str__(self):
        return (super().__str__() +
                f" Nganh hoc: {self.nganh_hoc} | Nam tot nghiep: {self.nam_tot_nghiep} | ")
    def inKQ(self,DS : list):
        w = 20
        header = (
        f"|{'Ten':<{w}}|{'Ngay sinh':<{w}}|{'Que quan':<{w}}|"
        f"{'Nganh hoc':<{w}}|{'Nam tot nghiep':<{w}}|"
    )
        dong_ke = "+" + "-" * (len(header) - 2) + "+"

        print("DANH SACH KY SU")
        print(dong_ke)
        print(header)
        print(dong_ke)

        for cn in DS:
        
            print(
            f"|{cn.ten:<{w}}|{cn.date:<{w}}|{cn.que:<{w}}|"
            f"{cn.nganh_hoc:<{w}}|{cn.nam_tot_nghiep:<{w}}|"
        )
        print(dong_ke)

    def nhap_DS(self):
        n = int(input("nhap so ky su muon them : "))
        for i in range(n):
            ten, date, que, nganh, nam = input(
            f"Nhap KS {i+1} (ten ngay que nganh nam): "
            ).split()
            self.DS.append(KySu(ten, int(date), que, nganh, int(nam)))
    def hien_thi_thong_tin(self):
        ds = [nv for nv in self.DS if nv.nam_tot_nghiep == max(nv.nam_tot_nghiep for nv in self.DS)]
        return ds
def main():
    ks1 = KySu("tung",12,"TH","IT",2025)
    ks1.nhap_DS()
    ks1.inKQ(ks1.DS)

    new_ds = ks1.hien_thi_thong_tin()
    print("KY SU CO NAM TOT NGHIEP CAO NHAT")
    ks1.inKQ(new_ds)
if __name__ =="__main__":
    main()
            
#     @staticmethod
#     def nhapKSU(DSKSU):
#         try:
#             name = input("Nhap ten: ").strip()
#             date = int(input("Nhap ngay sinh: "))
#             if not 1 <= date <= 31:
#                 raise ValueError("Ngay sinh khong hop le")

#             que = input("Nhap que quan: ").strip()
#             nganh_hoc = input("Nhap nganh hoc: ").strip()

#             nam_tn = int(input("Nhap nam tot nghiep: "))
#             if nam_tn <= 0:
#                 raise ValueError("Nam tot nghiep phai > 0")

#             ks = KySu(name, date, que, nganh_hoc, nam_tn)
#             DSKSU.append(ks)

#         except Exception as e:
#             print("Loi:", e)

#     @staticmethod
#     def nhapDS(DSKSU):
#         try:
#             n = int(input("Nhap so ky su muon them: "))
#             if n <= 0:
#                 raise ValueError("n phai > 0")

#             for _ in range(n):
#                 KySu.nhapKSU(DSKSU)

#         except Exception as e:
#             print("Loi:", e)

#     def tim_kiem(self,DSKSU):
#         max_nam = max([cn.nam_tot_nghiep for cn in DSKSU])
#         list_new = [cn for cn in DSKSU if cn.nam_tot_nghiep == max_nam]
#         return list_new
        
# def main():
#     ks1 = KySu("Tung", 12, "Ha Noi", "IT", 2026)
#     print(ks1)

#     DSKSU = []
#     KySu.nhapDS(DSKSU)
#     KySu.inKQ(ks1,DSKSU)
#     new_list = KySu.tim_kiem(ks1,DSKSU)
#     KySu.inKQ(ks1 , new_list)

# if __name__ == "__main__":
#     main()
