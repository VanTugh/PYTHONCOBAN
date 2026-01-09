from Bai4.distance import tinhkc
from Bai4.area import area

def main_2_4():
    print("\n--- BÀI 2.4: POINTS ---")
    try:
        x1 = float(input("Nhap x1: "))
        y1 = float(input("Nhap y1: "))
        x2 = float(input("Nhap x2: "))
        y2 = float(input("Nhap y2: "))
        x3 = float(input("Nhap x3: "))
        y3 = float(input("Nhap y3: "))

        AO = tinhkc(x1, 0, y1, 0)
        BO = tinhkc(x2, 0, y2, 0)
        CO = tinhkc(x3, 0, y3, 0)

        distances = {"A": AO, "B": BO, "C": CO}

        print(f"Điểm gần tâm O nhất: {min(distances, key=distances.get)}")
        print(f"Điểm xa tâm O nhất: {max(distances, key=distances.get)}")

        AB = tinhkc(x1, x2, y1, y2)
        BC = tinhkc(x2, x3, y2, y3)
        AC = tinhkc(x1, x3, y1, y3)

        if AB + BC > AC and AB + AC > BC and AC + BC > AB:
            print(f"Diện tích tam giác ABC: {area(x1, y1, x2, y2, x3, y3)}")
        else:
            print("Ba điểm không tạo thành tam giác")

    except ValueError:
        print("Vui lòng nhập số hợp lệ")

if __name__ == "__main__":
    main_2_4()
