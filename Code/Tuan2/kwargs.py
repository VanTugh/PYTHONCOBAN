import os

# Đề bài: Viết hàm thong_tin_sinh_vien(**kwargs) nhận vào các thông tin tùy ý của sinh viên (tên, tuổi, lớp...).
# In ra màn hình các thông tin đó theo định dạng: Key: Value.
def thong_tin_sinh_vien(**kwargs):
    for key,items in kwargs.items():
        print(f"{key} is {items}")

# Đề bài (CSS Generator): Viết hàm tao_css(selector, **kwargs) để tạo ra một chuỗi CSS.

# selector: Tên thẻ HTML hoặc ID/Class.

# **kwargs: Các thuộc tính CSS (Lưu ý: Python không dùng dấu gạch ngang - trong tên biến được, 
# nên người dùng sẽ truyền background_color, hàm phải tự đổi thành background-color).

# Input: tao_css("div.container", width="100px", background_color="red") Output: div.container { width: 100px; background-color: red; }
def tao_css(selector, **kwargs):
    khoa_trai ="{"
    print(f"{selector} {khoa_trai}")
    for key, value in kwargs.items():
        css = key.replace("_","-")
        print(f"{css} : {value} ;")
    print("}")

# Đề bài: Viết một hàm build_sql_query(table_name, **kwargs) để tự động tạo câu lệnh SQL SELECT dựa trên các điều kiện lọc.
# Mặc định là điều kiện bằng (=).
# Nếu tên tham số kết thúc bằng __gt (greater than), __lt (less than), hãy xử lý toán tử tương ứng (>, <).
# Input: build_sql_query("users", age__gt=18, city="Hanoi", status="active") 
# Output: SELECT * FROM users WHERE age > 18 AND city = 'Hanoi' AND status = 'active'
def build_sql_query(table_name, **kwargs):
    conditions = []
    
    for key, value in kwargs.items():
        operator = "=" # Mặc định
        column = key   # Mặc định tên cột là key
        
        # Xử lý các hậu tố đặc biệt (__gt, __lt)
        if key.endswith("__gt"):
            operator = ">"
            column = key[:-4] # Cắt bỏ 4 ký tự cuối (__gt)
        elif key.endswith("__lt"):
            operator = "<"
            column = key[:-4]
            
        # Xử lý giá trị chuỗi cần có dấu nháy đơn, số thì không cần
        if isinstance(value, str):
            value_str = f"'{value}'"
        else:
            value_str = str(value)
            
        conditions.append(f"{column} {operator} {value_str}")
    
    where_clause = " AND ".join(conditions)
    
    query = f"SELECT * FROM {table_name}"
    if where_clause:
        query += f" WHERE {where_clause}"
        
    return query
if __name__ == "__main__":
    os.system('cls')
    thong_tin_sinh_vien(masv = 123, tensv="NguyenTung")
    tao_css("div.container", width="100px", background_color="red")
    print(build_sql_query("users", age__gt=18, city="Hanoi", status="active"))