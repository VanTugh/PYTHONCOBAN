import pandas as pd
from pandas import DataFrame
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
def thong_ke_so_luong(df : DataFrame):
    so_luong_don_hang = df[df['OrderYear'] == 2023]
    dem_so_hang_hoa = so_luong_don_hang.shape[0]
    sp_ban_duoc = so_luong_don_hang['Quantity'].sum()
    doanh_thu = (so_luong_don_hang['Quantity'] * so_luong_don_hang['Price']).sum()
    ban_Chay_nhat = df.groupby('Product')['Quantity'].sum().idxmax()
    return dem_so_hang_hoa, sp_ban_duoc , doanh_thu, ban_Chay_nhat
def don_hang_2023(df : DataFrame):
    # df_new = df[df['OrderYear']==2023]
    new_df = df.loc[df['OrderYear'] == 2023]
    return new_df
def dem_so_don(df:DataFrame):
    dem = df.groupby('CustomerID')['Quantity'].sum()
    return dem
def tong_don(df:DataFrame):
    dem = df['Quantity'].sum()
    return dem
def inCUSTOMER(df:DataFrame):
    new =df['CustomerID'].unique()
    return new
def them_cot_moi(df:DataFrame):
    df['Revenue'] = [1,2,3,4,5]  
def tong_doanh_thu_theo_nam(df:DataFrame):
    df['ThanhTien'] = df['Quantity'] * df['Price']
    kq = df.groupby('OrderYear')['ThanhTien'].sum()
    return kq
def khach_Mua_nhieu(df:DataFrame):
    new = df.groupby('CustomerID')['Quantity'].sum().idxmax()
    return new
def sap_theo_doanh_thu(df:DataFrame):
    df['ThanhTien'] = df['Quantity'] * df['Price']
    df_sorted = df.sort_values(by='ThanhTien', ascending=False)
    return df_sorted
def ghi_file(df:DataFrame, filename):
    df.to_csv(filename)
def main():
    df = luu_data()
    print("Data ban dau la:")
    print(df)

    # so_luong ,sp ,thu, ban= thong_ke_so_luong(df)
    # print("so luong don hang la : ",so_luong)
    # print("tong san pham : ",sp)
    # print("tong doanh thu : ",thu)
    # print("sp ban chay nhat :", ban)
    # new_2023 = don_hang_2023(df)
    # print("cac don hang 2023 : \n",new_2023)

    # dem =dem_so_don(df)
    # print("so don cua moi khach : \n",dem)

    # tong = tong_don(df)
    # print("tong don : ", tong)
    new = inCUSTOMER(df)
    print("danh sach khong trung : \n",new)
    them_cot_moi(df)
    print(df)
    tien = tong_doanh_thu_theo_nam(df)
    print("theo nam \n",tien)
    khach = khach_Mua_nhieu(df)
    print("khach mua nhieu nhat la : ",khach)
    df_so = sap_theo_doanh_thu(df)
    print(df_so)
    
if __name__ =="__main__":
    main()