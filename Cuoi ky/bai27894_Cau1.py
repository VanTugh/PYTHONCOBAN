from typing import List
def nhap_lieu():
    while True:
        try:
            n = int(input("Nhap so luong tour (n>=5): "))
            if n >= 5:
                break
            print("Vui long nhap n >= 5!")
        except ValueError:
            print("Loi: Vui long nhap so nguyen.")

    ds = [
        {
            'ma_tour': input(f"\nNhap ma tour thu {i+1}: ").strip(),
            'ten_tour': input("  - Ten tour: ").strip(),
            'dia_diem': input("  - Dia diem: ").strip(),
            'ngay_kh': input("  - Ngay khoi hanh: ").strip(),
            'so_ngay': int(input("  - So ngay: "))
        }
        for i in range(n)
    ]
    return ds

def inKQ(tour):
    print("\n--- DANH SACH TOUR ---")
    for i in tour:
        print(i)

def them_gia_ve(danh_sach_tour):
    # SỬ DỤNG ENUMERATE ĐỂ LẤY SỐ THỨ TỰ (index) VÀ PHẦN TỬ (item)
    new_ds = [
        {
            **item, # Copy toàn bộ dữ liệu cũ
            'gia_ve': int(input(f"Nhap gia ve cho tour '{item['ten_tour']}' (thu {index+1}): "))
        }
        for index, item in enumerate(danh_sach_tour)
    ]
    return new_ds
def gia_ve_tb(tour):
    tong = sum(tou['gia_ve'] for tou in tour)
    return tong / len(tour)
def tao_du_lieu_gia():
    """Hàm trả về danh sách 5 tour mẫu để đỡ phải nhập tay"""
    return [
        {
            "ma_tour": "T01",
            "ten_tour": "Hà Nội - Hạ Long",
            "dia_diem": "Quảng Ninh",
            "ngay_kh": "30/04/2024",
            "so_ngay": 3
        },
        {
            "ma_tour": "T02",
            "ten_tour": "Đà Nẵng - Hội An",
            "dia_diem": "Đà Nẵng",
            "ngay_kh": "01/05/2024",
            "so_ngay": 4
        },
        {
            "ma_tour": "T03",
            "ten_tour": "Sài Gòn - Phú Quốc",
            "dia_diem": "Kiên Giang",
            "ngay_kh": "15/06/2024",
            "so_ngay": 3
        },
        {
            "ma_tour": "T04",
            "ten_tour": "Nha Trang Biển Gọi",
            "dia_diem": "Khánh Hòa",
            "ngay_kh": "20/05/2024",
            "so_ngay": 3
        },
        {
            "ma_tour": "T05",
            "ten_tour": "Sapa Mùa Lúa Chín",
            "dia_diem": "Lào Cai",
            "ngay_kh": "10/09/2024",
            "so_ngay": 2
        }
    ]
def sap(tour : List):
    tour.sort(key = lambda x : x['gia_ve'])
def tim_kiem(name:str, tour:List):
    name_list = [t for t in tour if t['dia_diem'] == name]
    return name_list
def sua(tour : List):
    return [
        {
            **t,
            'gia_ve' : t['gia_ve']*1.1 if t['so_ngay'] >= 4 else t['gia_ve']
        }
        for t in tour
    ]
def main():
    # tour = nhap_lieu()
    tour = tao_du_lieu_gia()
    inKQ(tour)
    print("\n--- CAP NHAT GIA VE ---")
    new_tour = them_gia_ve(tour)
    
    print("\n--- KET QUA SAU KHI THEM ---")
    inKQ(new_tour)

    tb = gia_ve_tb(new_tour)
    print(" gia ve trung binh : ",tb)
    sap(new_tour)
    print("sau khi sap :")
    inKQ(new_tour)
    new = tim_kiem("Khánh Hòa",new_tour)
    print(new)

    print("sau khi sua :")
    fix = sua(new_tour)
    inKQ(fix)
if __name__ == "__main__":
    main()