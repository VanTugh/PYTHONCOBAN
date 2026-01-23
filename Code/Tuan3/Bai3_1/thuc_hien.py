
def nhap_lieu(name = "X"):
    while True: 
        try :
            raw = input(f"Nhập các phần tử cho {name} (cách nhau bởi dấu cách): ")
            data = list(map(float , raw.split()))
            return data
        except ValueError:
            print("Lỗi: Dữ liệu nhập vào không phải số. Vui lòng nhập lại!")
def tong_cac_ptu(A):
    tong = 0
    for i in A:
        tong +=i
    return tong

def chen(A, index, value):
    A.append(0)
    i = len(A) -1
    while i > index :
        A[i] =A[i-1]
        i-=1
    A[index] = value
    return A
def xoa(A, index):
    n = len(A)
    for i in range(index, n-1):
        A[i] = A[i+1]
    A.pop()
    return A


def cong_cung_kich_thuoc(L, C):
    # cach 1:
    # A = []
    # if len(L) != len(C):
    #     return A 
    # else:
    #     for i in range(len(L)):
    #         A.append(L[i] + C[i])
    #     return A
    # cach 2 toi uu hon
    if len(L) != len(C):
        print("Lỗi: Hai mảng không cùng kích thước. Trả về mảng rỗng")
        return []
    return [x+y for x, y in zip(L,C)]