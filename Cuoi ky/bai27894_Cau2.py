class GiaoDich:
    def __init__(self, maGD, loaiGD, ngayGD, giaTri, loaiTS):
        self.maGD = maGD
        self.loaiGD = loaiGD
        self.ngayGD = ngayGD
        self.giaTri = giaTri
        self.loaiTS = loaiTS

    def __str__(self): 
        return f"| ma : {self.maGD} | loai giao dich : {self.loaiGD} | ngay : {self.ngayGD} | gia tri : {self.giaTri} | loai tai san : {self.loaiTS}"
    def __gt__(self, other):
        if self.loaiTS == other.loaiTS:
            return self.giaTri > 500_000_000 and other.giaTri <= 500_000_000
        return False


def nhap_ds():
    while True:
        n = int(input("Nhap so giao dich (n > 3): "))
        if n > 3:
            break

    ds = []
    for i in range(n):
        print(f"\nNhap giao dich thu {i+1}:")
        ma = input("Ma GD: ")
        loai = input("Loai GD (Mua/Ban): ")
        ngay = input("Ngay GD: ")
        gia = int(input("Gia tri GD: "))
        ts = input("Loai tai san: ")

        gd = GiaoDich(ma, loai, ngay, gia, ts)
        ds.append(gd)
    return ds


def loc_giao_dich_vang(ds):
    return [gd for gd in ds if gd.loaiTS.lower() == "vàng"]


def sap_xep_tang_dan(ds):
    ds.sort(key=lambda x: x.giaTri)


def ghi_file(ds):
    with open("VANG.TXT", "w", encoding="utf-8") as f:
        for gd in ds:
            f.write(str(gd) + "\n")
def fakedata():
    return [
        GiaoDich("GD01", "Mua", 1, 300_000_000, "Vàng"),
        GiaoDich("GD02", "Ban", 5, 800_000_000, "Vàng"),
        GiaoDich("GD03", "Mua", 10, 1_200_000_000, "Bat dong san"),
        GiaoDich("GD04", "Ban", 15, 450_000_000, "Vàng"),
        GiaoDich("GD05", "Mua", 20, 600_000_000, "Co phieu")
    ]


def main():
    # ds = nhap_ds()
    ds = fakedata()
    for i in ds:
        print(i)
    ds_vang = loc_giao_dich_vang(ds)

    sap_xep_tang_dan(ds)
    print("sau khi sap: ")
    for i in ds:
        print(i)

    print("\nDANH SACH GIAO DICH VANG:")
    for gd in ds_vang:
        print(gd)

    ghi_file(ds)


if __name__ == "__main__":
    main()
