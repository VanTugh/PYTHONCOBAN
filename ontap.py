from typing import Dict , List ,Tuple
# Câu hỏi: Bạn có một list các tuple chứa thông tin sinh viên: 
# Hãy sắp xếp list này theo điểm số (phần tử thứ 2 trong tuple) từ cao xuống thấp.
students = [('Tuan', 8.0), ('Nam', 9.5), ('Hoa', 7.5)]
students.sort(key= lambda x : x[1], reverse=True)
print(students)
# Câu hỏi (Sparse Matrix Representation): Tại sao Tuple có thể dùng làm key của Dictionary trong khi List thì không? 
# Hãy ứng dụng điều này để lưu trữ một ma trận thưa (ma trận kích thước lớn 1000x1000 nhưng hầu hết giá trị là 0,
# chỉ có vài điểm có giá trị). Yêu cầu: Tạo một cấu trúc dữ liệu lưu tọa độ (row, col) 
# có giá trị khác 0 và viết hàm get_value(matrix, row, col) trả về giá trị tại tọa độ đó (nếu không có trả về 0).
# Lưu trữ ma trận thưa bằng Dictionary với key là Tuple (row, col)
sparse_matrix = {
    (0, 5): 10,
    (100, 2): 99,
    (55, 60): 1
}
def get_value(matrix , row , col):
    return matrix.get((row, col) , 0)
# Câu hỏi: Viết một hàm nhận vào một list các số nguyên. 
# Hàm trả về một list mới chỉ chứa bình phương của các số chẵn, lập phương các số lẻ trong list ban đầu. 
# (Khuyến khích dùng List Comprehension).
a = [1,2,3,4,5,6,7,8,9]
b = [x ** 2 if x % 2 == 0 else x ** 3 for x in a]
print(b)
# Câu 3: Mức độ Vận dụng cao (High Application) - LeetCode 53
# Câu hỏi (Maximum Subarray): Cho một mảng số nguyên nums. Hãy tìm một mảng con liên tiếp (subarray) có tổng lớn nhất và trả về tổng đó. 
# Yêu cầu: Độ phức tạp thời gian là O(n).
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] Output: 6 (Mảng con là [4, -1, 2, 1])
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def Kadane(nums):
    nums_max = nums[0]
    max_curr = nums[0]
    for i in range(1, len(nums)):
        max_curr = max(nums[i], nums[i]+max_curr)
        nums_max = max(nums_max, max_curr)
    print(f"tong ket qua cua mang moi la : {nums_max}")
print(Kadane(nums))

