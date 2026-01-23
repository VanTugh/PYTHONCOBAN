import shutil
import os

def xu_ly():
    ROOT = "BAI44"
    SOURCE_CODE = r"C:\Users\welcome\OneDrive\Desktop\TAI LIEU HOC\TRÍ TUỆ NHÂN TẠO\PYTHON CBAN\Data\Image.data"
    DEST_FILE = "Data.dat"
    if not os.path.exists(SOURCE_CODE):
        print(f" khong tim thay {SOURCE_CODE}")
        return
    current = os.getcwd()
    dir_path = os.path.join(current, ROOT)
    dest_path = os.path.join(dir_path, DEST_FILE)
    try:
        print(f"tao thu muc moi {ROOT}")
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print(f"Da tao thu muc {ROOT}")
        else:
            print(f"{ROOT} da ton tai")
        print("copy file ne")
        shutil.copy(SOURCE_CODE, dest_path)
        if os.path.exists(dest_path):
            print("da copy thanh cong")
        else:
            print("loi tao file")
        if os.path.exists(dest_path):
            os.remove(dest_path)
            print("da xoa thanh cong")
        else:
            print("khong xoa duoc")
        if os.path.exists(dir_path):
            os.rmdir(dir_path) 
            print("Đã xóa thư mục.")
        else:
            print("Thư mục không tồn tại.")

    except Exception as e:
        print("Loi xu ly file:", e)

def main():
    xu_ly()
if __name__ == "__main__":
    main()

