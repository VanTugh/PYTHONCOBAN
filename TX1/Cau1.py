from typing import Dict , List
def nhap_lieu():
    cn_list = []
    while True:
        ma_cn = input("nhap ma cong nhan : ")
        ten_cn =input("nhap vap ten cong nhan :").strip()
        try:
            luong = int(input("nhap vao luong ngay : "))
            so_ngay_cong = int(input("nhap vao so ngay cong : "))
            phu_cap = int(input("nhap vao phu cap : "))
            luong_co_ban = luong * so_ngay_cong
        except ValueError:
            print("vui long nhap so hop le")
            continue
        cn={
            'maCN' : ma_cn,
            'hten' : ten_cn,
            'luong' :luong,
            'ngay_cong':so_ngay_cong,
            'phu_cap' : phu_cap,
            'luong_cb' : luong_co_ban
        }
        cn_list.append(cn)
        print("-"*30)
        while True:
            tt = input("ban co muon nhap tiep khong ? Y/N : ").strip().lower()
            if tt in ('y','n'):
                break
        if tt in ('n'):
            break
    return cn_list
def fakedata():
    cn_list = [
        {
            'maCN': '001',
            'hten': 'Tung',
            'luong': 12,
            'ngay_cong': 23,
            'phu_cap': 34,
            'luong_cb': 12 * 23
        },
        {
            'maCN': '002',
            'hten': 'Hoa',
            'luong': 1,
            'ngay_cong': 23,
            'phu_cap': 34,
            'luong_cb': 1 * 23
        },
        {
            'maCN': '003',
            'hten': 'Mai',
            'luong': 12,
            'ngay_cong': 3,
            'phu_cap': 34,
            'luong_cb': 12 * 3
        },
        {
            'maCN': '004',
            'hten': 'Lan',
            'luong': 2,
            'ngay_cong': 23,
            'phu_cap': 34,
            'luong_cb': 2 * 23
        },
        {
            'maCN': '005',
            'hten': 'Truc',
            'luong': 2,
            'ngay_cong': 3,
            'phu_cap': 34,
            'luong_cb': 2 * 3
        },
        {
            'maCN': '006',
            'hten': 'Cuc',
            'luong': 12,
            'ngay_cong': 2,
            'phu_cap': 3,
            'luong_cb': 12 * 2
        }
    ]
    return cn_list

def in_KQ(my_list : List):
    if not my_list:
        print("danh sach rong")
        return
    w_ma = 15
    w_so  = 15
    header =(
        f"|{'Ma cong nhan' :<{w_ma}} | {'Ten cong nhan' :<{w_ma}} |"
        f"{'Luong ngay':<{w_so}} | {'So ngay cong':<{w_so}} |"
        f"{'Phu cap':<{w_so}} | {'Luong co ban':<{w_so}} |"
    )
    dong_ke = "+"+"-"*(len(header) -2)+"+"
    print("DANH SACH CONG NHAN")
    print(dong_ke)
    print(header)
    print(dong_ke)
    for cn in my_list:
        row = (
            f"|{cn['maCN'] :<{w_ma}} | {cn['hten'] :<{w_ma}} |"
            f"{cn['luong']:<{w_so}} | {cn['ngay_cong']:<{w_so}} |"
            f"{cn['phu_cap']:<{w_so}} | {cn['luong_cb']:<{w_so}} |"
        )
        print(row)
    print(dong_ke)
def tim_tong_thu_nhap_lon_nhat(my_list : List) -> List:
    tong_lon_nhat = max((cn['luong_cb'] + cn['phu_cap']) for cn in my_list)
    dsach_cong_nhan = [cn for cn in my_list if (cn['luong_cb'] + cn['phu_cap']) == tong_lon_nhat]
    return dsach_cong_nhan
def dem_so_cong_nhan(my_list :List):
    dem = sum(1 for cn in my_list if (cn['luong'] > 0 and cn['ngay_cong'] >0 and cn['phu_cap'] > 0 ) and(cn['luong_cb'] + cn['phu_cap']) > 15)
    return dem

def main():
    # cn_list = 
    cn_list = fakedata()
    in_KQ(cn_list)
    dsach_can_tim = tim_tong_thu_nhap_lon_nhat(cn_list)
    print("Danh sach cong nhan cong tong thu lon nhat : ")
    in_KQ(dsach_can_tim)
    dem = dem_so_cong_nhan(cn_list)
    print(f"so cong nhan du dieu kien la : {dem}")

if __name__ == "__main__":
    main()
