class NGUOI:
    def __init__(self, hoten, tuoi, quoctich):
        self.hoten = hoten
        self.tuoi = tuoi
        self.quoctich = quoctich

class CAUTHU(NGUOI):
    def __init__(self, hoten, tuoi, quoctich, mact, vitri, ao, clb):
        super().__init__(hoten, tuoi, quoctich)
        self.mact = mact
        self.vitri = vitri
        self.ao = ao
        self.clb = clb

    def __str__(self):
        # Format in cho thẳng hàng
        return (f"| {self.mact:<5} | {self.hoten:<20} | {self.tuoi:<3} | "
                f"{self.quoctich:<12} | {self.vitri:<10} | "
                f"Ao: {self.ao:<3} | CLB: {self.clb.tenclb}")

class CAULACBO:
    def __init__(self, maclb, tenclb, hlv, namtl):
        self.maclb = maclb
        self.tenclb = tenclb
        self.hlv = hlv
        self.namtl = namtl
    
    def __str__(self):
        return f"CLB: {self.tenclb} (HLV: {self.hlv})"

def nhap_ds(clb):
    while True:
        try:
            n = int(input("Nhap so luong cau thu (n > 0): "))
            if n > 0: break
        except ValueError:
            print("Vui long nhap so!")
            
    ds = []
    for i in range(n):
        print(f"\n--- Nhap thong tin cau thu thu {i+1} ---")
        ma = input("Ma cau thu: ")
        ten = input("Ho ten: ")
        tuoi = int(input("Tuoi: "))
        qt = input("Quoc tich: ")
        vt = input("Vi tri: ")
        so_ao = int(input("So ao: "))
        
        ct = CAUTHU(ten, tuoi, qt, ma, vt, so_ao, clb)
        ds.append(ct)
    return ds

def inKQ(ds):
    print("-" * 90)
    for i in ds:
        print(i)
    print("-" * 90)

def fakedata(clb):
    return [
        CAUTHU("Cristiano Ronaldo", 39, "Bo Dao Nha", "CT01", "Tien dao", 10, clb),
        CAUTHU("Lionel Messi", 36, "Argentina", "CT02", "Tien dao", 30, clb),
        CAUTHU("Kylian Mbappe", 25, "Phap", "CT03", "Tien dao", 7, clb),
        CAUTHU("Jude Bellingham", 20, "Anh", "CT04", "Tien ve", 5, clb),
        CAUTHU("Pedri", 21, "Tay Ban Nha", "CT05", "Tien ve", 8, clb),
        CAUTHU("GONZALO", 18, "Tay Ban Nha", "CT06", "Tien dao", 19, clb),
    ]

def sua_CT(ds: list, name: str, so_ao_moi: int):
    found = False
    for ct in ds:
        # So sánh chuỗi (có thể dùng lower() để không phân biệt hoa thường)
        if ct.hoten.lower() == name.lower():
            print(f"\n[Update] Da tim thay {name}. Doi so ao {ct.ao} -> {so_ao_moi}")
            ct.ao = so_ao_moi
            found = True
            break # Tìm thấy rồi thì thoát vòng lặp cho tối ưu
            
    if not found:
        print(f"\n[Loi] Khong tim thay cau thu ten: {name}")
def nho_hon20(ds):
    new_ds = sum(1 for ct in ds if ct.tuoi <20)
    return new_ds
def sap(ds):
    ds.sort(key = lambda x : x.ao)
def main():
    clb = CAULACBO("001", "Real Madrid", "Carlo Ancelotti", 1902)
    
    # 1. Tạo dữ liệu giả
    ds = fakedata(clb)
    
    print("\n=== DANH SACH BAN DAU ===")
    inKQ(ds)
    
    # 2. Sửa số áo Ronaldo từ 10 thành 7
    sua_CT(ds, "Cristiano Ronaldo", 7)
    
    # 3. In lại để kiểm tra
    print("\n=== DANH SACH SAU KHI SUA ===")
    inKQ(ds)

    nho = nho_hon20(ds)
    print(f"SO CAU THU NHO HON 20 : {nho}")
    
    sap(ds)
    print("\n=== DANH SACH SAU KHI SAP ===")
    inKQ(ds)

if __name__ == "__main__":
    main()