import os
import numpy as np
from typing import List, Tuple
Matrix = List[List[float]]
def doc_file(filename : str ) -> Tuple[int, int, Matrix]:
    if not os.path.exists(filename):
        print(" file khong ton tai ")
        return
    try :
        with open(filename , 'r', encoding='utf-8') as f:
            header = f.readline().split()
            if not header:
                print(" file rong ")
                return
            n = int(header[0])
            m = int(header[1])
            a = []
            for i in f:
                row= list(map(float , i.split()))
                a.append(row)
        return n,m ,a
    except ValueError:
        print("file loi roi")
        return 0,0,[]
def inKQ(n : int , m:int, matrix: Matrix) ->None:
    print(f"ket qua : n = {n} va m = {m}")
    for row in matrix:
        print(row)
    # trung_binh_cot = np.mean(a, axis=0)
    # print(trung_binh_cot)
    so_dong = len(matrix)
    so_cot =len(matrix[0])
    trung_binh_cot = [sum(row[j] for row in matrix )/ so_dong for j in range(so_cot)]
    print(trung_binh_cot)

def main():
    TEN_FILE = r"C:\Users\welcome\OneDrive\Desktop\TAI LIEU HOC\TRÍ TUỆ NHÂN TẠO\PYTHON CBAN\Data\DATA54.txt"
    n,m,matrix = doc_file(TEN_FILE)
    inKQ(n,m,matrix)


if __name__ == "__main__":
    main()