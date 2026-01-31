from typing import List
import itertools
def nhap_lieu()-> List[float]:
    a = float(input("Nhap so a: "))
    b = float(input("Nhap so b: "))
    c = float(input("Nhap so c: "))
    return [a, b, c]
def hoan_vi (my_list : List):
    return list(itertools.permutations(my_list))

# cau 2
def nhap_lieu_2() -> List[float]:
    my_list =[
        num for num in map(float, input("Nhap cac so cach nhau boi dau cach: ").split(" "))
    ]
    return my_list
def check_theo_dieu_kien(new_list: List[float]) -> int:
    if not new_list:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(new_list)):
        if new_list[i] == new_list[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    return max_len
# bai 3
def kiem_tra_theo_yc(my_list: List[float]) :
    # co_tang = False
    # co_giam = False
    # co_bang = False
    # for cap in zip(my_list, my_list[1:]):
    #     if cap[0] < cap[1]:
    #         co_tang = True
    #     elif cap[0] > cap[1]:
    #         co_giam = True
    #     else:
    #         co_bang = True
    # # if co_tang and not co_giam and not co_bang:
    # #     print("Cac cap so tai vi tri chan tang dan.")
    # # elif co_giam and not co_tang and not co_bang:
    # #     print("Cac cap so tai vi tri chan giam dan.")   
    # # elif co_bang and not co_tang and not co_giam:
    # #     print("Cac cap so tai vi tri chan bang nhau.")
    # # else:
    # #     print("Khong co tinh chat")
    if all(my_list[i] < my_list[i + 1] for i in range(len(my_list) - 1)):
        print("Cac cap so tai vi tri chan tang dan.")
    elif all(my_list[i] > my_list[i + 1] for i in range(len(my_list) - 1)):
        print("Cac cap so tai vi tri chan giam dan.")
    elif all(my_list[i] == my_list[i + 1] for i in range(len(my_list) - 1)):
        print("Cac cap so tai vi tri chan bang nhau.")
    else:
        print("Khong co tinh chat")

def hien_thi_danh_sach(my_list: List[float]):
    print("Cac so da nhap la:")
    for num in my_list:
        print(num, end=" ")
    print()
def main():
    # my_list = nhap_lieu()
    # ket_qua = hoan_vi(my_list)
    # print("Cac hoan vi cua ba so la:")
    # for perm in ket_qua:
    #     print(perm)

    new_list = nhap_lieu_2()
    hien_thi_danh_sach(new_list)
    count = check_theo_dieu_kien(new_list)
    print(f"So luong cap so bang nhau lien tiep la: {count}")
    kiem_tra_theo_yc(new_list)
if __name__ == "__main__":
    main()
