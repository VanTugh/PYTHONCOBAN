import os
import shutil
from typing import List, Tuple
Matrix= List[List[float]]

def doc_du_lieu(filename : str )->None:
    if not os.path.exists(filename):
        print(f"khong tim thay {filename}")
        return
    with open(filename , 'r' , encoding= 'utf-8') as f:
        content = f.read()
        print(content)
def ghi_du_lieu(filename : str ) ->Tuple[int,int,Matrix]:
    if not os.path.exists(filename):
        print(f"khong tim thay {filename}")
        return
    try:
        with open(filename , 'r' , encoding= 'utf-8') as f:
            header = f.readline().split()
            if not header:
                print("file rong")
                return
            n= int(header[0])
            m= int(header[1])
            print(f" n = {n} va m = {m} ")
            a = []
            for line in f:
                row = list(map(float , line.split()))
                a.append(row)
            return n, m, a
    except ValueError:
        print("file loi roi")
        return 0,0,[]
def dem_so_0(a : Matrix ) -> Matrix:
    count = sum(row.count(0) for row in a)
    print(f"co {count} phan tu 0 trong file")
    tbc = [sum(col) / len(col) for col in zip(*a)]
    a_new  =[
        [
            tbc[j] if val == 0 else val for j, val in enumerate(row)
        ]
        for row in a
    ]
    print(a_new)
    return a_new
def ghi_file(filename : str, matrix : Matrix , n: int, m: int) -> None:
    try:
        if not os.path.exists(filename):
            print(f"khong tim thay {filename} -> tao moi ")
            with open(filename , 'w' , encoding='utf-8') as f:
                f.write(f" {n} {m} " + "\n")
                for row in matrix:
                    line = " ".join(map(str, row))
                    f.write(line +"\n")
                print("da ghi thanh cong")
    except PermissionError:
        print("loi truy cap")
def Create_File(fname : str , rows, r_n, r_m):
    with open(fname, 'w') as f:
        f.write(f"{r_n} {r_m} + " "\n")
        f.writelines(" ".join(map(str, row)) + "\n" for row in rows)
def check(fname : str) -> bool:
    if os.path.exists(fname):
        print(f"da co {fname} nay roi ")
        return True
    else:
        print(f"chua co {fname} nay dau ")
        return False
def file_split(a_new : Matrix , m: int) -> None:
    part1= a_new[:100]
    dodai1 = len(part1)
    part2 = a_new[100:]
    dodai2 = len(part2)
    PART1 = "P1.txt"
    PART2 = "P2.txt"
    Create_File(PART1,part1,dodai1,m)
    Create_File(PART2,part2,dodai2,m)
    if check(PART1) and check(PART2):
        print("split ok")
    else:
        print("chua split duoc")
def tao_moi_folder(FOLDER: str , SOUCE_CODE : str , OUT_PUT:str) -> None:
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)
        print(f"chua co folder {FOLDER} -> tao moi")
    else:
        print(f"{FOLDER} da ton tai")
    print("Copy")
    current = os.getcwd()
    dir_path = os.path.join(current, FOLDER)
    dest_path = os.path.join(dir_path, OUT_PUT)
    if not os.path.exists(dir_path):
        print(f"khong tim thay file goc {SOUCE_CODE}")
    else:
        shutil.copy(SOUCE_CODE , dest_path)
        print("copy thanh cong ")
    print("xoa ne")
    if os.path.exists(dest_path):
        os.remove(dest_path)
        print("xoa thanh cong")
    else:
        print("loi k xoa duoc")

def main():
    filename = r"C:\Users\welcome\OneDrive\Desktop\TAI LIEU HOC\TRÍ TUỆ NHÂN TẠO\PYTHON CBAN\Data\Image.data"
    doc_du_lieu(filename)
    n,m,a = ghi_du_lieu(filename)
    a_new = dem_so_0(a)
    OUT_PUT= "image2.txt"
    ghi_file(OUT_PUT, a_new, n,m)
    file_split(a_new,m)
    folder = "BAI55"
    SOURCE_CODE = r"C:\Users\welcome\OneDrive\Desktop\TAI LIEU HOC\TRÍ TUỆ NHÂN TẠO\PYTHON CBAN\image2.txt"
    OUT_PUT_COPY = "image2_copy.txt"
    tao_moi_folder(folder,SOURCE_CODE , OUT_PUT_COPY)


if __name__ == "__main__":
    main()
