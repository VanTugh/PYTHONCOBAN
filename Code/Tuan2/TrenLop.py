from typing import List, Tuple, Set, Dict
Matrix_Dict = Dict[str , str]
Matrix = List[float]
Matrix_Tuple = Tuple[float, ...]
Matrix_Set = Set[float]
def nhap_lieu() -> Tuple[int, Matrix]:
    n = int(input("nhap so phan tu muon them : "))
    print("nhap cac phan tu cho ma tran")
    matrix = [float(input(f"nhap vao phan tu thu {i} : ")) for i in range(1, n + 1)]
    return n, matrix
def chen_vi_tri(matrix : Matrix) -> Matrix:
    try:
        k = int(input(" nhap vao vi tri muon chen : "))
        if k > len(matrix):
            print(f"vuot qua kich thuoc mang")
        else:
            value = float(input(f"nhap vao gia tri muon chen vao {k} : "))
            matrix.insert(k,value)
        return matrix
    except ValueError:
        print("loi kieu du lieu")
        return []
def xoa_ptu_chan(matrix : Matrix) -> Matrix:
    new_matrix = [a for a in matrix if a %2 != 0]
    return new_matrix
def sap_xep(matrix: Matrix) -> None:
    matrix.sort()
def test_matrix() -> None:
    lst = [
    {(0, 1): 5},
    {(2, 3): 1},
    {(4, 5): 9}]
    lst.sort(key= lambda x : next(iter(x.values())))
    print(lst)

def main():
    n, matrix = nhap_lieu()
    print("ma tran ban dau:", matrix)
    sap_xep(matrix)
    print("ket qua sau khi sap:", matrix)
    test_matrix()
    insert_matrix = chen_vi_tri(matrix)
    print("ma tran sau khi them : " , insert_matrix)
    remove_matrix = xoa_ptu_chan(matrix)
    print("ma tran sau khi xoa cac phan tu chan  : " , remove_matrix)
def nhap_lieu_tuple()->Tuple[int, Matrix_Tuple]:
    try :
        n =int(input("nhap so phan tu : "))
        matrix = tuple(
            float(input(f"nhap vao cac phan tu {i} cho ma tran : ")) for i in range(1,n+1)
            )
        return n, matrix
    except ValueError:
        print("loi nhap lieu !")
        return 0, []
def sap_xep(matrix : Matrix_Tuple)-> Matrix_Tuple:
    new_matrix = sorted(matrix, reverse=True)
    return new_matrix
def dem_so_phan_tu_chan(matrix : Matrix_Tuple) -> int:
    # count = 0
    # for i in matrix:
    #     if i %2==0:
    #         count+=1
    count_val = sum(1 for i in matrix if i % 2 ==0)
    return count_val
def check_vtri(matrix : Matrix_Tuple) -> bool:
    try:
        check = False
        c = float(input("nhap phan tu muon tim : "))
        if c in matrix:
            print(f"da tim thay {c} trong {matrix}")
            check = True
        else:
            print(f"khong tim thay {c}")
        return check
    except ValueError:
        print("loi nhap lieu")
        return None
def binh_ga(matrix: Matrix_Tuple) -> Tuple[int, int, int]:
    min_ga = min(matrix)
    max_ga = max(matrix)
    count = sum(1 for i in matrix if i == 12)
    print("min cua tupe : ", min_ga)
    print("max cua tupe : ", max_ga)
    print("ga = 12 cua tupe co : ", count)
    return min , max , count
def thao_tac_voi_SET() -> Set:
    A = {1,"Tung", 2,3 ,7, 97 , "Hoa"}
    B = {1,2,3,4,5, "Tung", "Haha"}
    C = A.union(B)
    D = A.difference(B)
    E = B.difference(A)
    F = A.intersection(B)
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Hop : {C}")
    print(f"Co A ma khong co B: {D}")
    print(f"Co B ma khong co A: {E}")
    print(f"Giao cua A va B = {F}")
def nhap_lieu_Tu_dien() -> Matrix_Dict :
    try :
        n = int(input("nhap vao so sinh vien muon them : "))
        danh_sach = {
        input(f"nhap id sinh vien thu {i+1}: ").strip():
        input(f"nhap ten sinh vien thu {i+1}: ").strip()
        for i in range(n)
        }
        return danh_sach
    except ValueError:
        print("Loi kieu du lieu ")
        return {}
def inKQ(matrix: Matrix_Dict) -> None :
    print("DANH SACH SINH VIEN ")
    for k , v in matrix.items():
        print(f"{k} : {v}")
def TD():
    new_matrix = nhap_lieu_Tu_dien()
    inKQ(new_matrix)
    boo = getTT("2023601002", new_matrix)
def getTT(id : str, matrix : Matrix_Dict) -> bool :
    check = False
    if id in matrix :
        check = True
        print(f"id : {matrix[id]}")
    return check

def tuple_test():
    n, matrix = nhap_lieu_tuple()
    print("ma tran sau khi tao : ",matrix)
    new_matrix = sap_xep(matrix)
    print("sau khi sap : ", new_matrix)
    count = dem_so_phan_tu_chan(matrix)
    print("so phan tu chan la : ", count)
    check = check_vtri(matrix)
    print(check)
    min, max , count  = binh_ga(matrix)
def nhap_lieu_TD() -> Matrix_Dict :
    try:
        date = input("nhap vao thoi gian : ").strip()
        time = input("nhap vao thoi gian thuc : hh/mm/..")
        server = input("nhap vao server muon luu : ")
        name = input("nhap name : ")
        password = input("nhap pass : ")
        a = {
            "date" : date,
            "time" : time,
            "server" : server,
            "name" : name,
            "password" :password
        }
        return a
    except ValueError:
        print("Loi kieu du lieu ")
        return {}
def ADD_TT(key : str,value : str ,matrix : Matrix_Dict) -> None:
    matrix.update([(key,value)])
    print("ket qua sau khi them : ")
    inKQ(matrix)
def TD_main():
    new_matrix = nhap_lieu_TD()
    inKQ(new_matrix)
    ADD_TT("status", "active",new_matrix)
def STRING_NHAP_DEM() -> Tuple[str , int]:
    string = input("nhap vao sau ky tu : ").split()
    count = sum(1 for i in string)
    return string, count
def string_name():
    chuoi, count = STRING_NHAP_DEM()
    print("chuoi vua nhap : ", chuoi)
    print(f"co {count} tu")
    matrix = DINH_NGHIA_DICT(chuoi)
    print("Tu dien moi la : ", matrix)
def DINH_NGHIA_DICT(chuoi : str)-> dict:
    matrix = {
        key : chuoi.count(key)
        for key in chuoi
    }
    return matrix
def HOP_LE(chuoi: str) -> bool:
    check = False
    chuoi , count = STRING_NHAP_DEM()
    matrix = DINH_NGHIA_DICT(chuoi)
    print(matrix)
    
if __name__ == "__main__":
    # main()
    # tuple_test()
    # thao_tac_voi_SET()
    # TD()
    #TD_main()
    string_name()
