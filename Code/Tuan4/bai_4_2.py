def nhap_lieu(name="X"):
    try:
        a = input(f"Hay nhap cac gia tri cho {name}: ")
        if not a.strip():
            return []
        c = set(a.split())
        return c
    except Exception: 
        print("Loi nhap lieu")
        return []
def check(A, B):
    ca_hai_ban = A.intersection(B)
    print("SV đăng ký cả 2 bàn:", ca_hai_ban)
    tong_hop = A.union(B)
    print("Danh sách tổng hợp:", tong_hop)
    chi_ban_1 = A.difference(B)
    print("Chỉ đăng ký bàn 1:", chi_ban_1)
def main():
    A = nhap_lieu("A")
    if not A:  
        print("Danh sach rong!")
        return
    B = nhap_lieu("B")
    if not B:  
        print("Danh sach rong!")
        return
    check(A,B)
if __name__ == "__main__":
    main()
    