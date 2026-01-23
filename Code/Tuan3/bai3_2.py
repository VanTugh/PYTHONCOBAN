def create_matrix(lst, n, m):
    """Chuyển list thành ma trận n dòng m cột."""
    if len(lst) < n * m:
        return None, "Không đủ phần tử để tạo ma trận"
    return [lst[i * m : (i + 1) * m] for i in range(n)], "Thành công"
def hien_thi_ket_qua(matrix, message, n, m, len_lst):
    if matrix is None:
        print(f"Lỗi: {message}")
        print(f"(Cần {n*m} phần tử, nhưng list chỉ có {len_lst})")
    else:
        print(f"Ma trận {n}x{m} thu được:")
        for row in matrix:
            print(*row) 
def lay_input():
    try:
        a = list(map(int, input("Nhập list (các số cách nhau bởi dấu cách): ").split()))
        print(f"-> List nhận được (k={len(a)}): {a}")
        n = int(input("Nhập số dòng n: "))
        m = int(input("Nhập số cột m: "))
        return a, n, m
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào không hợp lệ!")
        return None, None, None
def main():
    print("--- MATRIX FROM LIST ---")
    lst, n, m = lay_input()
    if lst is None: return 
    matrix_result, msg = create_matrix(lst, n, m)
    hien_thi_ket_qua(matrix_result, msg, n, m, len(lst))

if __name__ == "__main__":
    main()





# import numpy as np
# a = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6]
# n, m = 3, 4
# # Cách làm của dân chuyên nghiệp:
# try:
#     # Bước 1: Lấy đúng số phần tử cần thiết (n*m phần tử đầu tiên)
#     data = np.array(a[:n*m]) 
#     # Bước 2: Reshape lại thành (n, m)
#     matrix = data.reshape(n, m)
#     print("Ma trận Numpy:\n", matrix)
# except ValueError:
#     print("Không thể reshape")