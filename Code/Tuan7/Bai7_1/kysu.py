from person import Person

class KySu(Person):
    def __init__(self, ten, date, que, nganh_hoc, nam_tot_nghiep):
        super().__init__(ten, date, que)
        self.nganh_hoc = nganh_hoc
        self.nam_tot_nghiep = nam_tot_nghiep

    def __str__(self):
        return (super().__str__() +
                f" Nganh hoc: {self.nganh_hoc} | Nam tot nghiep: {self.nam_tot_nghiep} | ")
    
    def inKQ(self, DSKSU):
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

        for cn in DSKSU:
            row = (
            f"|{cn.ten:<{w}}|{cn.date:<{w}}|{cn.que:<{w}}|"
            f"{cn.nganh_hoc:<{w}}|{cn.nam_tot_nghiep:<{w}}|"
            )
            print(row)

        print(dong_ke)

            
    @staticmethod
    def nhapKSU(DSKSU):
        try:
            name = input("Nhap ten: ").strip()
            date = int(input("Nhap ngay sinh: "))
            if not 1 <= date <= 31:
                raise ValueError("Ngay sinh khong hop le")

            que = input("Nhap que quan: ").strip()
            nganh_hoc = input("Nhap nganh hoc: ").strip()

            nam_tn = int(input("Nhap nam tot nghiep: "))
            if nam_tn <= 0:
                raise ValueError("Nam tot nghiep phai > 0")

            ks = KySu(name, date, que, nganh_hoc, nam_tn)
            DSKSU.append(ks)

        except Exception as e:
            print("Loi:", e)

    @staticmethod
    def nhapDS(DSKSU):
        try:
            n = int(input("Nhap so ky su muon them: "))
            if n <= 0:
                raise ValueError("n phai > 0")

            for _ in range(n):
                KySu.nhapKSU(DSKSU)

        except Exception as e:
            print("Loi:", e)

    def tim_kiem(self,DSKSU):
        max_nam = max([cn.nam_tot_nghiep for cn in DSKSU])
        list_new = [cn for cn in DSKSU if cn.nam_tot_nghiep == max_nam]
        return list_new
        
def main():
    ks1 = KySu("Tung", 12, "Ha Noi", "IT", 2026)
    print(ks1)

    DSKSU = []
    KySu.nhapDS(DSKSU)
    KySu.inKQ(ks1,DSKSU)
    new_list = KySu.tim_kiem(ks1,DSKSU)
    KySu.inKQ(ks1 , new_list)

if __name__ == "__main__":
    main()
