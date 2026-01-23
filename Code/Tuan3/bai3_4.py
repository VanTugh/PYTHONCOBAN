def nhap_mang(ten="Arr"):
    try:
        raw = input(f"Nhập mảng {ten} (các số cách nhau bởi dấu cách): ")
        data = list(map(int, raw.split()))
        return data
    except ValueError:
        return []

def hien_thi_test(index, a, b, c):
    print(f"Test Case {index}:")
    print(f"Input A (n={len(a)}): {a}")
    print(f"Input B (m={len(b)}): {b}")
    print(f"=> Output C      : {c}")
    print("-" * 50)

def merge_sorted_lists(a, b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    n = len(a_sorted) 
    m = len(b_sorted)
    i, j = 0, 0
    c = []
    
    while i < n and j < m:
        if a_sorted[i] < b_sorted[j]:
            c.append(a_sorted[i]) 
            i += 1
        else:
            c.append(b_sorted[j])
            j += 1
            
    c.extend(a_sorted[i:])
    c.extend(b_sorted[j:])
    return c

def main():
    print("--- BÀI 3.4: MERGE TWO SORTED LISTS ---\n")
    
    print(">>> CHẠY TEST CASE TỰ ĐỘNG")
    test_cases = [
        {
            "desc": "n < m",
            "a": [1, 3, 5],       
            "b": [2, 4, 6, 8, 10] 
        },
        {
            "desc": "n > m",
            "a": [1, 2, 3, 9, 10], 
            "b": [4, 5]            
        },
        {
            "desc": "n = m",
            "a": [1, 5, 9],
            "b": [2, 6, 10]
        },
        {
            "desc": "Có số trùng nhau & Số âm",
            "a": [-5, 0, 5, 5],
            "b": [-2, 0, 2, 5]
        }
    ]

    for i, test in enumerate(test_cases, 1):
        a = test["a"]
        b = test["b"]
        c = merge_sorted_lists(a, b)
        hien_thi_test(f"{i} ({test['desc']})", sorted(a), sorted(b), c)
    print("\n>>> NHẬP TAY TỪ BÀN PHÍM")
    user_a = nhap_mang("A")
    user_b = nhap_mang("B")
    
    if user_a is not None and user_b is not None:
        user_a.sort()
        user_b.sort()
        result = merge_sorted_lists(user_a, user_b)
        hien_thi_test("User Input", user_a, user_b, result)
    else:
        print("Lỗi nhập liệu, bỏ qua phần nhập tay.")

if __name__ == "__main__":
    main()