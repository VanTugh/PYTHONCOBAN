from typing import Dict , List

def nhap_lieu():
    while True:
        try:
            n = int(input("nhap so san pham muon them : "))
            if n <= 0:
                raise ValueError("san pham > 0")
            cn_list = []
            for i in range(n):
                maSP = input(f"nhap vao ma san pham thu {i+1} : ")
                soLuong = int(input("nhap vao so luong ton kho : "))
                cn = {
                    'maSP' : maSP,
                    'soLuong' : soLuong
                }
                cn_list.append(cn)
            return cn_list
        except Exception as e:
            print(" loi : ", e)
def inKQ(sp_list : List):
    if not sp_list :
        print("data rong")
        return
    w_ma = 15
    w_so =20
    header =(
        f"| {'Ma san pham':<{w_ma}} | {'So luong ton kho':<{w_so}} |"
    )
    dong_ke = "+"+"-"*(len(header) -2)+"+"
    print("DANH SACH SAN PHAM")
    print(dong_ke)
    print(header)
    print(dong_ke)
    for sp in sp_list:
        row =(
            f"| {sp['maSP']:<{w_ma}} | {sp['soLuong']:<{w_so}} |"
        )
        print(row)
    print(dong_ke)

def nhap_lieu_2():
    while True:
        try:
            n = int(input("nhap so san pham muon them : "))
            if n <= 0:
                raise ValueError("san pham > 0")
            cn_list = []
            for i in range(n):
                maSP = input(f"nhap vao ma san pham thu {i+1} : ")
                tenSP = (input("nhap vao ten san pham : "))
                cn = {
                    'maSP' : maSP,
                    'tenSP' : tenSP
                }
                cn_list.append(cn)
            return cn_list
        except Exception as e:
            print(" loi : ", e)
def inKQ_2(sp_list : List):
    if not sp_list :
        print("data rong")
        return
    w_so =20
    header =(
        f"| {'Ma san pham':<{w_so}} | {'Ten san pham':<{w_so}} |"
    )
    dong_ke = "+"+"-"*(len(header) -2)+"+"
    print("DANH SACH SAN PHAM")
    print(dong_ke)
    print(header)
    print(dong_ke)
    for sp in sp_list:
        row =(
            f"| {sp['maSP']:<{w_so}} | {sp['tenSP']:<{w_so}} |"
        )
        print(row)
    print(dong_ke)
def check(my_list : List , masp:str):
    if not my_list:
        return False
    for sp in my_list:
        if sp['maSP'] == masp:
            return True
def xu_ly(my_list: List, masp: str):
    kq = check(my_list, masp)
    if kq:
        print(f"San pham co ma {masp} ton tai trong danh sach")
        for sp in my_list:
            if sp['maSP'] == masp:
                sp['soLuong'] = 100
                break
    else:
        my_list.append({
            'maSP': masp,
            'soLuong': 100
        })
    return my_list
def xoa_SP(my_list: List):
    new_list = [sp for sp in my_list if sp['soLuong'] != 0]
    return new_list
def chuyen_doi(my_list: List):
    maSP = [sp['maSP'] for sp in my_list]
    soLuong = [sp['soLuong'] for sp in my_list]
    return maSP , soLuong
def intheoYC(my_list: List, soLuong : List):
    print(my_list[:3])
    print(soLuong[3:])
def main():
    sp_list = nhap_lieu()
    inKQ(sp_list)
    # sp_list2 = nhap_lieu_2()
    # inKQ_2(sp_list2)
    # new_one = xu_ly(sp_list , 'ST001')
    # inKQ(new_one)
    # new_one = xoa_SP(sp_list)
    # inKQ(new_one)
    masp , soLuong = chuyen_doi(sp_list)
    print("Ma san pham : ", masp)
    print("So luong ton kho : ", soLuong)
    intheoYC(masp , soLuong)
if __name__ == "__main__":
    main()
