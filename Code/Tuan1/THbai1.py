import math
def bai_1_1_convert():
    print("--- BÀI 1.1: CONVERT ---")
    try:
        n = int(input("Nhập số nguyên n (ít hơn 5 chữ số): "))
        s = str(n)
        length = len(s)
        
        if length >= 5:
            print("Vui lòng nhập số ít hơn 5 chữ số!")
            return

        # Tạo danh sách tên các hàng theo thứ tự ngược từ đơn vị lên
        hang = ["đơn vị", "chục", "trăm", "ngàn"]
        
        # Đảo ngược chuỗi số để khớp index với danh sách 'hang'
        # Ví dụ: 1523 -> "3251" -> s_rev[0]='3' (đơn vị), s_rev[3]='1' (ngàn)
        s_rev = s[::-1] 
        
        ket_qua = []
        # Duyệt từ hàng cao nhất xuống thấp nhất (để in xuôi)
        for i in range(length - 1, -1, -1):
            digit = s_rev[i]
            ten_hang = hang[i]
            ket_qua.append(f"{digit} {ten_hang}")
            
        print("Cách đọc: " + " ".join(ket_qua))
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên.")

# Chạy thử
bai_1_1_convert()

def bai_1_2_distance():
    print("\n--- BÀI 1.2: DISTANCE ---")
    try:
        # Nhập liệu trên 1 dòng hoặc từng dòng đều được
        x1 = float(input("Nhập x1: "))
        y1 = float(input("Nhập y1: "))
        x2 = float(input("Nhập x2: "))
        y2 = float(input("Nhập y2: "))

        # 1. Khoảng cách Euclidean
        d_euclidean = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # 2. Khoảng cách Manhattan
        d_manhattan = abs(x2 - x1) + abs(y2 - y1)

        # 3. Khoảng cách Cosine
        # Công thức: C = 1 - (A.B) / (||A|| * ||B||)
        tu_so = x1*x2 + y1*y2
        mau_so = math.sqrt(x1**2 + y1**2) * math.sqrt(x2**2 + y2**2)
        
        if mau_so == 0:
            d_cosine = "Không xác định (do vector 0)"
        else:
            d_cosine = 1 - (tu_so / mau_so)

        print(f"Khoảng cách Euclidean: {d_euclidean:.4f}")
        print(f"Khoảng cách Manhattan: {d_manhattan:.4f}")
        print(f"Khoảng cách Cosine:    {d_cosine}")

    except ValueError:
        print("Lỗi: Vui lòng nhập số thực.")
def bai_1_3_equations():
    print("\n--- BÀI 1.3: EQUATIONS ---")
    try:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))

        # Trường hợp a = 0 -> Trở thành phương trình bậc 1: bx + c = 0
        if a == 0:
            if b == 0:
                if c == 0:
                    print("Phương trình có vô số nghiệm.")
                else:
                    print("Phương trình vô nghiệm.")
            else:
                x = -c / b
                print(f"Phương trình bậc 1 có nghiệm x = {x}")
        
        # Trường hợp a != 0 -> Phương trình bậc 2
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                print("Phương trình vô nghiệm thực.")
            elif delta == 0:
                x = -b / (2*a)
                print(f"Phương trình có nghiệm kép x = {x}")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")

    except ValueError:
        print("Lỗi nhập liệu.")
def bai_1_4_sequence():
    print("\n--- BÀI 1.4: SEQUENCE ---")
    try:
        x = float(input("Nhập số thực x: "))
        n = int(input("Nhập số nguyên n: "))
        S = 0
        if n % 2 != 0:
            print("n là số lẻ, S = 0")
        else:
            tong = 0
            S = 2016 * x
            for i in range(2,n+1):
                tu_so = x **i
                mau_so= 3 ** (i-1)
                tong += tu_so/mau_so
            S +=tong
            print(f"Giá trị biểu thức S = {S}")
    except ValueError:
        print("Lỗi nhập liệu.")
bai_1_4_sequence()
# Hàm phụ trợ: Kiểm tra số nguyên tố
def is_prime(num):
    if num < 2:
        return False
    # Kiểm tra từ 2 đến căn bậc 2 của num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def is_palindrome(num):
    s = str(num)
    return s == s[::-1]
def bai_1_5_license_plate():
    print("\n--- BÀI 1.5: LICENSE PLATE ---")
    try:
        n = int(input("Nhập số nguyên n (ít hơn 7 chữ số): "))
        # Kiểm tra điều kiện đầu vào
        if len(str(n)) >= 7:
            print("Số nhập vào phải ít hơn 7 chữ số.")
            return
        check_prime = is_prime(n)
        check_palindrome = is_palindrome(n)
        if check_prime and check_palindrome:
            print(f"{n} là số HỢP LỆ (vừa là số nguyên tố, vừa đối xứng).")
        else:
            print(f"{n} KHÔNG hợp lệ.")
            # Giải thích thêm cho rõ ràng
            if not check_prime:
                print(f"- {n} không phải số nguyên tố.")
            if not check_palindrome:
                print(f"- {n} không phải số đối xứng.")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên.")