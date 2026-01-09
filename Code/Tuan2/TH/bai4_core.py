from Bai4.core import Point,distance_to_origin , triangle_area
def get_point(label : str )->Point:
    raw = input(f"nhap toa do {label} (x,y)").split()
    return Point(float(raw[0]), float(raw[1]))
def main():
    try:
        pA = get_point("A")
        pB = get_point("B")
        pC = get_point("C")
        points = [pA,pB,pC]
        labels = {pA : "A", pB : "B", pC : "C"}
        closest = min(points, key=distance_to_origin)
        farthest = max(points, key=distance_to_origin)

        print(f"\n Gần tâm O nhất: Điểm {labels[closest]} {closest}")
        print(f" Xa tâm O nhất : Điểm {labels[farthest]} {farthest}")

        area = triangle_area(pA, pB, pC)
        print(f" Diện tích tam giác: {area:.2f}")

    except (ValueError, IndexError):
        print("Lỗi nhập liệu!")

if __name__ == "__main__":
    main()