# def xu_ly_chuoi():
#     try :
#         S = input(" nhap chuoi S : ").split()
#         Q = input(" nhap chuoi Q : ").split()
#         check = False
#         if len(S) == 0 or len(Q) == 0:
#             raise ValueError(" khong duoc de rong")
#         for i in S:
#             for j in Q:
#                 if j == i:
#                     check = True
#                     break
#         if check == True:
#             print(" Q la tap con cua S")
#         else:
#             print(" Q k la tap con cua S")
#     except ValueError:
#         print(" nhap lai")

# if __name__ == "__main__":
#     xu_ly_chuoi()
from typing import Tuple, List, Dict

def xu_ly_chuoi() -> Tuple[List[str], List[str]]:
    try:
        raw_s = input("Nhap chuoi S: ").strip()
        raw_q = input("Nhap chuoi Q: ").strip()
        if not raw_s or not raw_q:
            raise ValueError("Chuỗi không được để trống")
        return raw_s.split(), raw_q.split()
    except ValueError as e:
        print(f"Lỗi nhập liệu: {e}")
        return [], []

def process_string_data(s: List[str], q: List[str]) -> None:
    set_s = set(s)
    set_q = set(q)
    is_s_in_q = set_s.issubset(set_q)
    print(f"Tap hop cac tu cua S la tap con cua Q: {is_s_in_q}")
    p = f"{' '.join(s)} {' '.join(q)}"
    p = p.replace("Ha", "Ba")
    print(f"Modified P: {p}")
    words_dict = {k: x for k, x in enumerate(p.split())}
    print("Dictionary ket qua:", words_dict)

if __name__ == "__main__":
    s_list, q_list = xu_ly_chuoi()
    if s_list and q_list:
        process_string_data(s_list, q_list)
    else:
        print("Chương trình dừng do lỗi nhập liệu.")