import pandas as pd
def luu_data():
    data = {
        'OrderID': [1001, 1002, 1003, 1004, 1005],
        'CustomerID': ['C001', 'C002', 'C003', 'C001', 'C004'],
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Mouse', 'Laptop'],
        'Quantity': [1, 2, 1, 5, 1],
        'Price': [800, 20, 50, 20, 800],
        'OrderYear': [2023, 2021, 2022, 2023, 2023]
    }
    new_data = pd.DataFrame(data)
    return new_data
def thong_ke_so_luong(df):
    so_luong_don_hang = df[df['OrderYear'] == 2023]
    dem_so_hang_hoa = so_luong_don_hang.shape[0]
    dem_so_luong_SP = so_luong_don_hang['Quantity'].sum()
    doanh_thu = so_luong_don_hang['Quantity'] * so_luong_don_hang['Price']
    ban_chay_nhat = (df.groupby('Product')['Quantity'].sum().idxmax())
    return dem_so_hang_hoa, dem_so_luong_SP, doanh_thu, ban_chay_nhat

def main():
    df = luu_data()
    print("Data ban dau la:")
    print(df)
    # df.to_csv('orders.csv', index = False)
    # print("Luu file thanh cong")
    so_luong_hang_hoa , so_luong_SP , doanh_thu,ban_chay_nhat = thong_ke_so_luong(df)
    print(f"So luong don hang nam 2023 la: {so_luong_hang_hoa}")
    print(f"So luong san pham ban duoc nam 2023 la: {so_luong_SP}")
    print("Doanh thu nam 2023 la:", doanh_thu)
    print("Don hang ban chay nhat la:" , ban_chay_nhat)
if __name__ == "__main__":
    main()