import os
from typing import List, Tuple, Union
Matrix = List[List[float]]
def nhap_ma_tran() ->Tuple[int, int, Matrix]:
    try:
        n = int(input(" nhap so dong : "))
        m = int(input(" nhap so cot : "))
        matrix =[]
        for i in range(n):
            while True:
                try:
                    raw = input(f"nhap dong {i+1} : ")
                    row = list(map(float ,  raw.split() ))
                    if len(row) != m:
                        print(f" phai du {m} chu so")
                        continue
                    matrix.append(row)
                    break
                except ValueError:
                    print(" chi nhap so thuc ")
        return n, m, matrix
    except ValueError:
        print(" loi kich thuoc ")
        return 0, 0, []

def ghi_file(filename : str , n: int , m: int , matrix : Matrix):
    try:
        with open(filename, 'w' , encoding='utf-8') as f:
            f.write(f"{n} {m}\n")
            for row in matrix:
                line = " ".join(map(str ,row))
                f.write(line +"\n")
    except IOError as e:
        print(f"Lỗi ghi file: {e}")

def main():
    TEN_FILE = r"C:\Users\welcome\OneDrive\Desktop\TAI LIEU HOC\TRÍ TUỆ NHÂN TẠO\PYTHON CBAN\Data\bai5_1.txt"
    n, m, matrix = nhap_ma_tran()
    if matrix:
        ghi_file(TEN_FILE, n, m, matrix)

if __name__ == "__main__":
    main()