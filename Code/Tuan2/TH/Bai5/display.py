def input_vector(name="X"):
    print(f"Nhập vector {name} (x1 x2 x3): ", end="")
    try:
        parts = list(map(float, input().split()))
        if len(parts) != 3: raise ValueError("Phải nhập đủ 3 toạ độ")
        return tuple(parts)
    except ValueError as e:
        print("Lỗi nhập liệu:", e)
        return (0.0, 0.0, 0.0)

def show_vector(v, label="Vector"):
    print(f"{label} = ({v[0]}, {v[1]}, {v[2]})")