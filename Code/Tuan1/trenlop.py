import math
import os

def xoa_man_hinh():
    os.system('cls' if os.name == 'nt' else 'clear')

def nhap_so_thuc(thong_bao):
    while True:
        try:
            return float(input(thong_bao))
        except ValueError:
            print("Lỗi: Vui lòng nhập số!")

def giai_pt_bac_2(a, b, c):
    if a == 0:
        if b == 0:
            return "Phương trình vô nghiệm" if c != 0 else "Phương trình có vô số nghiệm"
        return f"Phương trình bậc 1 có 1 nghiệm: x = {-c / b}"

    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm thực"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        return f"Phương trình có 2 nghiệm phân biệt:\n x1 = {x1}\n x2 = {x2}"

def ktra_SNT():
    while True:
        try:
            a = int(input("Nhập số a: "))
            break
        except ValueError:
            print("Lỗi: vui lòng nhập số nguyên!")

    if a < 2:
        return False

    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True
def tinhP(n, x):
    while n < 20 or n > 30:
        print(f"Giá trị n={n} không hợp lệ (phải từ 20 đến 30).")
        try:
            n = int(input("Mời nhập lại n = "))
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên!")
    P1 = 2022 * math.pow(x, n)
    P2 = 0
    for i in range(1, n + 1):
        P2 += i / math.pow(x, i)
    return P1 + P2


if __name__ == "__main__":
    xoa_man_hinh()
    print("--- GIẢI PHƯƠNG TRÌNH BẬC 2 ---")
    a = nhap_so_thuc("Nhập a: ")
    b = nhap_so_thuc("Nhập b: ")
    c = nhap_so_thuc("Nhập c: ")
    print(giai_pt_bac_2(a, b, c))

    print("\n--- KIỂM TRA SỐ NGUYÊN TỐ ---")
    print("Kết quả:", ktra_SNT())

    x = float(input(" nhap x = "))
    n = int(input("nhap n = "))
    print(f"ket qua P = {tinhP(n,x)}")
