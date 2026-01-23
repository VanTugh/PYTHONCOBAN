import os
def doc_file(filename: str ) ->None:
    if not os.path.exists(filename):
        print(" file k ton tai ")
        return
    try:
        with open(filename , 'r', encoding='utf-8') as f:
            header =  f.readline().split()
            if not header:
                print(" file rong")
                return
            n = int(header[0])
            m = int(header[1])
            a = []
            for i in f:
                row = list(map(float, i.split()))
                a.append(row)

            print(f"ket qua : n = {n} va m = {m}")
            for row in a:
                print(row)
    except ValueError:
        print("file loi roi")

def main():
    TEN_FILE = r"C:\Users\welcome\OneDrive\Desktop\TAI LIEU HOC\TRÍ TUỆ NHÂN TẠO\PYTHON CBAN\Data\bai5_1.txt"
    doc_file(TEN_FILE)

if __name__ == "__main__":
    main()