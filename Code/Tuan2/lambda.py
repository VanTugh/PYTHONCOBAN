import os
# Đề bài: Viết một chương trình sử dụng lambda để tìm số lớn nhất giữa hai số nhập vào. 
# So sánh nó với cách viết hàm def thông thường.

tim_max = lambda a, b : a if a>b else b
print(tim_max(2,4))

# Đề bài: (Sắp xếp danh sách phức tạp) Cho một danh sách các từ điển (dictionary) 
# chứa thông tin cầu thủ bóng đá:
players = [{"name": "Ronaldo", "goals": 30}, {"name": "Messi", "goals": 35}, {"name": "Neymar", "goals": 20}]
# Hãy sắp xếp danh sách này theo số bàn thắng (goals) giảm dần sử dụng lambda.
sap_xep = sorted(players, key= lambda x : x["goals"], reverse=True) 
print(sap_xep)

# Đề bài: (Bài toán sắp xếp đa tiêu chí - Thường gặp trong LeetCode) Cho một danh sách các chuỗi: 
# Hãy sắp xếp danh sách này theo tiêu chí sau:
# Độ dài chuỗi tăng dần.
# Nếu độ dài bằng nhau, sắp xếp theo thứ tự bảng chữ cái ngược (Z -> A).
# Gợi ý: Python cho phép so sánh Tuple. (1, 'b') < (2, 'a') là True.
os.system('cls')
data = ["apple", "banana", "cherry", "date", "fig"]
data.sort(key=lambda x: x, reverse=True)
data.sort(key=lambda x : len(x))  
# sap binh thg : data.sort(key=lambda x: (len(x), x))  voi len(x),x  = 5, "apple"
print(data)