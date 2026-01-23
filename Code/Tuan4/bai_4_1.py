def nhap_lieu(name="X"):
    try:
        a = input("Hay nhap cac gia tri vao day: ")
        if not a.strip():
            return []
        c = a.split()
        return c
    except Exception: 
        print("Loi nhap lieu")
        return []

def convert(A):
    C = []
    for i in A:
        C.append(int(i))
    return C  

def TBC(A):  
    if not A:  
        return 0
    tong = 0
    for i in A:
        tong += i
    return tong / len(A)

def main():
    A = nhap_lieu("A")
    if not A:  
        print("Danh sach rong!")
        return
    
    C = convert(A)
    print("Danh sach so:", C)
    
    TBCv = TBC(C)  
    print("Trung binh cong:", TBCv)
from typing import Tuple
import statistics

def process_number_tuple(raw_data: Tuple[str, ...]) -> None:
    print("\n=== BÀI 4.1: TUPLE PROCESSING ===")
    
    # Pythonic: Dùng map() để ép kiểu hàng loạt. Nhanh hơn vòng lặp for.
    num_tuple: Tuple[int, ...] = tuple(map(int, raw_data))
    
    # Pythonic: Dùng statistics.mean() hoặc sum()/len()
    avg_val = statistics.mean(num_tuple) if num_tuple else 0
    
    print(f"Original : {raw_data}")
    print(f"Converted: {num_tuple}")
    print(f"Average  : {avg_val:.2f}")
def xu_ly_ham_nang_cao():
    A = nhap_lieu("A")
    if not A:  
        print("Danh sach rong!")
        return
    process_number_tuple(A)
if __name__ == "__main__":
    main()
    xu_ly_ham_nang_cao()