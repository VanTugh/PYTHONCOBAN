import os
# Đề bài: Viết một chương trình đếm số lần một hàm được gọi. Sử dụng một biến toàn cục count. 
# Viết hàm click_button() mỗi lần chạy sẽ tăng count lên 1 và in ra "Đã click X lần".
os.system('cls')
count = 0
def click_button():
    global count
    count+=1
    return count
print(f" lan click thu : {click_button()}")

# Đề bài: (Tạo bộ nhớ không dùng Global - Ứng dụng trong Decorator/Factory) 
# Hãy viết một hàm tao_tai_khoan(so_du_ban_dau). Hàm này trả về hai hàm con: nap_tien(so_tien) và rut_tien(so_tien).
# Hai hàm con này phải truy cập và thay đổi được so_du_ban_dau (được lưu trong Closure). Yêu cầu: Không dùng biến global, không dùng class.
# Tình huống: nap, rut = tao_tai_khoan(100) nap(50) -> Số dư: 150 rut(20) -> Số dư: 130


def tao_tai_khoan(so_du_ban_dau):
    so_du = so_du_ban_dau
    def nap_tien(so_tien):
        nonlocal so_du
        so_du += so_tien
        print(f"Nạp {so_tien}. Số dư mới: {so_du}")
    def rut_tien(so_tien):
        nonlocal so_du
        if so_tien < so_du:
            so_du -= so_tien
            print(f"Rút {so_tien}. Số dư mới: {so_du}")
        else:
            print("Số dư không đủ!")
    return nap_tien, rut_tien
# Test
print("--- TEST TÀI KHOẢN ---")
my_deposit, my_withdraw = tao_tai_khoan(100) # Khởi tạo tài khoản với 100k

my_deposit(50)  # Output: 150
my_withdraw(30) # Output: 120
my_withdraw(200) # Output: Không đủ