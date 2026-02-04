from abc import ABC,abstractmethod
class NGUOI:
    def __init__(self, hoten, tuoi, quoctich):
        self.hoten = hoten
        self.tuoi = tuoi
        self.quoctich = quoctich
class CAULACBO:
    def __init__(self, maclb, tenclb, hlv, namtl):
        self.maclb = maclb
        self.tenclb = tenclb
        self.hlv = hlv
        self.namtl = namtl
    
    def __str__(self):
        return f"CLB: {self.tenclb} (HLV: {self.hlv})"
class CAUTHU(NGUOI, ABC):
    def __init__(self, hoten, tuoi, quoctich, mact, ao, clb):
        super().__init__(hoten, tuoi, quoctich)
        self.mact = mact
        self.ao = ao
        self.clb = clb
    def __str__(self):
        return (f"| {self.mact:<5} | {self.hoten:<20} | {self.tuoi:<3} | "
                f"{self.quoctich:<12} | "
                f"{self.ovr()} | {self.tinh_luong()} |"
                f"Ao: {self.ao:<3} | CLB: {self.clb.tenclb}|"
                )
    @abstractmethod
    def ovr(self):
        pass
    @abstractmethod
    def luong(self):
        pass
    def tinh_luong(self):
        return self.ovr() * self.luong()
    def __gt__(self,other):
        return self.ovr() > other.ovr()
    def __eq__(self,other):
        return self.ovr() == other.ovr()
class TIENDAO(CAUTHU):
    def ovr(self):
        return 95
    def luong(self):
        return 100000
class TIENVE(CAUTHU):
    def ovr(self):
        return 93
    def luong(self):
        return 80000
class HAUVE(CAUTHU):
    def ovr(self):
        return 90
    def luong(self):
        return 70000
def inKQ(ds):
    print("-" * 92)
    for i in ds:
        print(i)
    print("-" * 92)

def fakedata(clb):
    ds = [
        # --- TIỀN ĐẠO (OVR 95, Lương cao nhất) ---
        TIENDAO("Cristiano Ronaldo", 39, "Bo Dao Nha", "FW01", 7, clb),
        TIENDAO("Lionel Messi", 37, "Argentina", "FW02", 10, clb),
        TIENDAO("Erling Haaland", 23, "Na Uy", "FW03", 9, clb),
        TIENDAO("Kylian Mbappe", 25, "Phap", "FW04", 7, clb),

        # --- TIỀN VỆ (OVR 93) ---
        TIENVE("Kevin De Bruyne", 32, "Bi", "MF01", 17, clb),
        TIENVE("Luka Modric", 38, "Croatia", "MF02", 10, clb),
        TIENVE("Jude Bellingham", 20, "Anh", "MF03", 5, clb),

        # --- HẬU VỆ (OVR 90) ---
        HAUVE("Virgil van Dijk", 32, "Ha Lan", "DF01", 4, clb),
        HAUVE("Sergio Ramos", 37, "Tay Ban Nha", "DF02", 4, clb),
        HAUVE("Alphonso Davies", 23, "Canada", "DF03", 19, clb),
    ]
    return ds 
def dem_cau_thu(ds):
    tien_dao = sum(1 for ct in ds if ct.ovr() == 95)
    tien_ve = sum(1 for ct in ds if ct.ovr() == 93)
    hau_ve = sum(1 for ct in ds if ct.ovr() == 90)
    return tien_dao, tien_ve ,hau_ve
def tim_cau_thu(ds):
    nho = min(ct.tuoi for ct in ds)
    lon = max(ct.tuoi for ct in ds)
    list_nho =[ct for ct in ds if ct.tuoi == nho]
    list_lon = [ct for ct in ds if ct.tuoi == lon]
    return list_nho, list_lon
def sap_nho(ds):
    ds.sort(key = lambda x : x.tuoi)
def sap_lon(ds:list):
    ds.sort(key = lambda x : x.tuoi,reverse=True)
def them_thuoc_tinh(ds):
    for i, ct in enumerate(ds):
        ct.so_ban_thang = int(
            input(f"Nhap so ban thang cho cau thu {ct.hoten}: ")
        )
def sap_theo_vi_tri(ds):
    thu_tu ={
        TIENDAO : 1,
        TIENVE : 2,
        HAUVE :3
    }
    ds.sort(key = lambda ct : thu_tu[type(ct)])
def luu_file(ds,filename):
    with open(filename,'w',encoding='utf-8')as f:
        for i in ds:
            f.write(str(i) +"\n")
def main():
    clb = CAULACBO("001", "Real Madrid", "Carlo Ancelotti", 1902)
    ds = fakedata(clb)
    inKQ(ds)
    td1 = TIENDAO("Neymar",29,"Brazil","ST04",10,"PSG")
    tv2 = TIENVE("Rodri",34,"Spain","MF04",10,"MC")
    if td1>tv2:
        print("lon hon")
    elif td1 == tv2:
        print("bang nhau")
    else:
        print("nho hon")
    t1,t2,t3 =dem_cau_thu(ds)
    print(f"{t1} - {t2} - {t3}")
    nho, lon = tim_cau_thu(ds)
    print("danh sach nho tuoi nhat")
    inKQ(nho)
    print("danh sach lon tuoi nhat")
    inKQ(lon)
    sap_lon(ds)
    print("sap lon")
    inKQ(ds)
    sap_nho(ds)
    print("sap nho")
    inKQ(ds)
    them_thuoc_tinh(ds)
    inKQ(ds)
    sap_theo_vi_tri(ds)
    print("ket qua sau khi xep theo vi tri : ")
    inKQ(ds)

    filename = r"C:\Users\welcome\OneDrive\Desktop\TAI LIEU HOC\TRÍ TUỆ NHÂN TẠO\PYTHON CBAN\Cauthu.txt"
    luu_file(ds,filename)
if __name__ =="__main__":
    main()