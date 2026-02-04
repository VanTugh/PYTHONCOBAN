from typing import List

def inKQ(ds: List):
    print("DANH SACH:")
    for i in ds:
        print(i)


def diemthi(ds: List):
    max_diem = max(i['diem_thi'] for i in ds)
    return [i for i in ds if i['diem_thi'] == max_diem]


def fakedata():
    return [
        {"ma_sv": "SV01", "ho_ten": "Nguyen Van An", "nam_sinh": 2003, "gioi_tinh": "Nam", "que_quan": "Ha Noi", "diem_thi": 9.2},
        {"ma_sv": "SV02", "ho_ten": "Tran Thi Binh", "nam_sinh": 2004, "gioi_tinh": "Nu", "que_quan": "Hai Phong", "diem_thi": 8.5},
        {"ma_sv": "SV03", "ho_ten": "Le Van Cuong", "nam_sinh": 2002, "gioi_tinh": "Nam", "que_quan": "Nam Dinh", "diem_thi": 7.8},
        {"ma_sv": "SV04", "ho_ten": "Pham Thi Dao", "nam_sinh": 2005, "gioi_tinh": "Nu", "que_quan": "Thai Binh", "diem_thi": 9.2},
        {"ma_sv": "SV05", "ho_ten": "Do Van Em", "nam_sinh": 2003, "gioi_tinh": "Nam", "que_quan": "Ha Nam", "diem_thi": 6.9},
        {"ma_sv": "SV06", "ho_ten": "Bui Thi Giang", "nam_sinh": 2004, "gioi_tinh": "Nu", "que_quan": "Bac Ninh", "diem_thi": 8.9},
        {"ma_sv": "SV07", "ho_ten": "Hoang Van Hung", "nam_sinh": 2001, "gioi_tinh": "Nam", "que_quan": "Thanh Hoa", "diem_thi": 9.5},
        {"ma_sv": "SV08", "ho_ten": "Vu Thi Lan", "nam_sinh": 2006, "gioi_tinh": "Nu", "que_quan": "Ha Noi", "diem_thi": 7.2},
        {"ma_sv": "SV09", "ho_ten": "Nguyen Van Minh", "nam_sinh": 2002, "gioi_tinh": "Nam", "que_quan": "Quang Ninh", "diem_thi": 8.0},
        {"ma_sv": "SV10", "ho_ten": "Tran Thi Nhung", "nam_sinh": 2004, "gioi_tinh": "Nu", "que_quan": "Hai Duong", "diem_thi": 9.5}
    ]
def xoa_theoma(masv : str, ds : List):
    new_list = [i for i in ds if i['ma_sv'] != masv]
    return new_list

def main():
    ds = fakedata()
    inKQ(ds)

    print("\nSINH VIEN CO DIEM THI CAO NHAT:")
    cao_nhat = diemthi(ds)
    inKQ(cao_nhat)

    print("\nXOA SINH VIEN:")
    xoa_sv = xoa_theoma('SV01',ds)
    inKQ(xoa_sv)

if __name__ == "__main__":
    main()
