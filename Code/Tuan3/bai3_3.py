def tron_danh_sach(a, b):
    ket_qua = []
    for x, y in zip(a, b):
        ket_qua.extend([x, y])
    ket_qua.extend(a[len(b):])
    ket_qua.extend(b[len(a):])
    return ket_qua
def hien_thi_test_case(index, a, b, ket_qua):
    print(f"Test Case {index}:")
    print(f"Input A (n={len(a)}): {a}")
    print(f"Input B (m={len(b)}): {b}")
    print(f"=> Output: {ket_qua}")
def main():
    print("--- BÀI 3.3: TRỘN DANH SÁCH (INTERLEAVE LISTS) ---\n")
    test_cases = [
        {
            "mo_ta": "A ngắn hơn B (Đề bài)",
            "a": ['a', 'b', 'c'],
            "b": [1, 2, 3, 4, 5]
        },
        {
            "mo_ta": "A dài hơn B",
            "a": [10, 20, 30, 40, 50],
            "b": ['x', 'y']
        },
        {
            "mo_ta": "A bằng B",
            "a": ["Hà Nội", "Đà Nẵng"],
            "b": ["HCM", "Cần Thơ"]
        },
        {
            "mo_ta": "A rỗng",
            "a": [],
            "b": [1, 2, 3]
        },
        {
            "mo_ta": "B rỗng",
            "a": [1, 2, 3],
            "b": []
        }
    ]
    for i, test in enumerate(test_cases, 1):
        a = test["a"]
        b = test["b"]
        ket_qua = tron_danh_sach(a, b)
        hien_thi_test_case(i, a, b, ket_qua)

if __name__ == "__main__":
    main()