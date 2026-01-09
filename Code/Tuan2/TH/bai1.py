import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def hop_le(n):
    return 1000000 <= n <= 99999999

def doi_xung(n):
    s = str(n)
    return s == s[::-1]

def bai2_1(s, e):
    while s > e or not hop_le(e):
        s = int(input("Nhap lai s: "))
        e = int(input("Nhap lai e: "))

    tong = 0
    for i in range(s, e + 1):
        if doi_xung(i) and is_prime(i):
            tong += i
    return tong

print(bai2_1(100, 80000000))


import math

def is_prime(n):
    if n < 2: 
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_palindromes(s, e):
    """Sinh các số đối xứng trong khoảng [s, e]"""
    res = []
    for length in range(len(str(s)), len(str(e)) + 1):
        half_len = (length + 1) // 2
        start = 10**(half_len - 1)
        end = 10**half_len
        for i in range(start, end):
            pal = int(str(i) + str(i)[-2::-1])
            if s <= pal <= e:
                res.append(pal)
    return res

def bai2_1_toi_uu(s, e):
    tong = 0
    for n in generate_palindromes(s, e):
        if is_prime(n):
            tong += n
    return tong

print(bai2_1_toi_uu(100, 80_000_000))


#########
import math
import time

def is_prime(n):
    """Kiểm tra số nguyên tố tối ưu"""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Kiểm tra từ 5 đến sqrt(n), bước nhảy 6 (tối ưu hơn)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_palindromes_in_range(min_val, max_val):
    """Sinh số đối xứng chỉ trong khoảng cần tìm, không sinh thừa"""
    def create_palindrome(half, odd_length):
        """Tạo số đối xứng từ nửa đầu"""
        if odd_length:
            return int(str(half) + str(half)[-2::-1])
        return int(str(half) + str(half)[::-1])
    
    palindromes = []
    min_len = len(str(min_val))
    max_len = len(str(max_val))
    
    for length in range(min_len, max_len + 1):
        half_len = (length + 1) // 2
        start = 10**(half_len - 1)
        end = 10**half_len
        
        for half in range(start, end):
            # Tạo số đối xứng độ dài chẵn và lẻ
            for odd in [False, True]:
                if odd and length % 2 == 0:
                    continue
                pal = create_palindrome(half, odd)
                
                # Kiểm tra trong khoảng và đủ độ dài
                if min_val <= pal <= max_val and len(str(pal)) == length:
                    palindromes.append(pal)
    
    return palindromes

def bai2_1_tot_nhat(s, e):
    """Phiên bản tối ưu nhất"""
    # Kiểm tra điều kiện đầu vào
    if s > e or s < 1000000 or e > 99999999:
        raise ValueError("Khoảng không hợp lệ!")
    
    total = 0
    count = 0
    
    # Chỉ sinh và xử lý các số đối xứng trong khoảng
    for pal in generate_palindromes_in_range(s, e):
        if is_prime(pal):
            total += pal
            count += 1
    
    return total, count  # Trả về cả tổng và số lượng tìm được

# Test và so sánh hiệu năng
if __name__ == "__main__":
    # Test với khoảng nhỏ để kiểm tra
    start_time = time.time()
    result1, count1 = bai2_1_tot_nhat(1000000, 2000000)
    time1 = time.time() - start_time
    
    start_time = time.time()
    result2, count2 = bai2_1_tot_nhat(1000000, 10000000)
    time2 = time.time() - start_time
    
    print(f"Khoảng 1M-2M: {count1} số, tổng = {result1}, thời gian: {time1:.3f}s")
    print(f"Khoảng 1M-10M: {count2} số, tổng = {result2}, thời gian: {time2:.3f}s")
    
    # So sánh với code gốc (chỉ chạy với khoảng nhỏ để tránh treo máy)
    def bai2_1_original(s, e):
        total = 0
        for i in range(s, e + 1):
            s_str = str(i)
            if s_str == s_str[::-1]:
                if is_prime(i):
                    total += i
        return total
    
    start_time = time.time()
    result3 = bai2_1_original(1000000, 1100000)  # Chỉ 100k số
    time3 = time.time() - start_time
    print(f"\nSo sánh với duyệt tuần tự (100k số):")
    print(f"Code cũ: {time3:.3f}s, Code mới: {time1:.3f}s")
    print(f"Tốc độ nhanh hơn {time3/time1:.1f} lần")