# Câu 1: Mức độ Hiểu (Understanding)
# Câu hỏi: Sự khác biệt giữa việc truy cập my_dict['key'] và my_dict.get('key') là gì? Khi nào nên dùng cái nào?
# Đáp án:
# my_dict['key']: Truy cập trực tiếp. Nếu key không tồn tại, chương trình sẽ báo lỗi KeyError và dừng lại. 
# -> Dùng khi bạn chắc chắn key tồn tại.
# my_dict.get('key'): Truy cập an toàn. Nếu key không tồn tại, nó trả về None (hoặc giá trị mặc định do bạn quy định) chứ không báo lỗi.
# -> Dùng khi không chắc chắn key có tồn tại hay không.


# Câu 2: Mức độ Vận dụng (Application)
# Câu hỏi: Cho một chuỗi ký tự: s = "hello world". Hãy viết hàm trả về một dictionary
# đếm số lần xuất hiện của từng ký tự trong chuỗi (không tính khoảng trắng).
# Output mong muốn: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

my_string = input(" nhap chuoi muon dem :")
my_dict = {}
for i in my_string:
    if i == " ":
        continue
    my_dict[i] = my_dict.get(i,0) + 1
sort_dict = dict(sorted(my_dict.items()))
print(sort_dict)
