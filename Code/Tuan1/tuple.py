# Câu hỏi: Bạn có một list các tuple chứa thông tin sinh viên: 
# Hãy sắp xếp list này theo điểm số (phần tử thứ 2 trong tuple) từ cao xuống thấp.
students = [('Tuan', 8.0), ('Nam', 9.5), ('Hoa', 7.5)]
students.sort(key=lambda x :x[1], reverse=False)
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

def get_value(matrix, r, c):
    # Dùng phương thức .get() của dict, default là 0
    return matrix.get((r, c), 0)

# Test
print(get_value(sparse_matrix, 0, 5))   # Output: 10
print(get_value(sparse_matrix, 0, 0))   # Output: 0 (Vì không lưu trữ -> hiểu là 0)