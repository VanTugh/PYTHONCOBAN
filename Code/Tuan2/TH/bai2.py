import os
from Bai2.QuyDoi.QuyDoi import vnd_to_foreign

def main_2_3():
    print("\n--- BÀI 2.3: FINANCE PACKAGE ---")
    try:
        miles = float(input("Nhập số dặm bay: "))
        price_per_mile = float(input("Nhập số tiền VND/1 dặm: "))
        
        total_vnd = miles * price_per_mile
        print(f"Tổng tiền VNĐ: {total_vnd:,.0f} đ")
        
        # Gọi hàm từ package
        exchange_data = vnd_to_foreign(total_vnd)
        
        print("Quy đổi ngoại tệ:")
        for curr, val in exchange_data.items():
            print(f"- {curr}: {val:,.2f}")

    except ValueError:
        print("Lỗi nhập liệu.")

if __name__ == "__main__":
    main_2_3()