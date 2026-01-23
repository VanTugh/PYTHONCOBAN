def dem_phan_tu_dang_so(data_tuple):
    # item.isdigit() trả về True (1) nếu chuỗi chỉ chứa số, False (0) nếu không
    return sum(1 for item in data_tuple if item.isdigit())

def main():
    print("--- BÀI TOÁN: TUPLE & NUMERIC STRINGS ---")
    try:
        raw_input = input("Nhập các phần tử của mảng a (cách nhau bởi dấu cách): ")
        if not raw_input.strip():
            a = [] # Xử lý trường hợp nhập rỗng
        else:
            a = raw_input.split()
        print(f"\n1. Mảng a (List) : {a}")
        b = tuple(a)
        print(f"2. Tuple b       : {b}")
        so_luong = dem_phan_tu_dang_so(b)
        print(f"\n-> Có {so_luong} phần tử dạng số trong b.")
        cac_so = [x for x in b if x.isdigit()]
        if cac_so:
            print(f"   (Đó là: {', '.join(cac_so)})")
    except Exception as e:
        print(f"Lỗi: {e}")
def run_test_cases():
    print("\n\n>>> CHẠY TEST CASE TỰ ĐỘNG")
    test_cases = [
        ["123", "abc", "030", "a1"],   # Mixed (Example)
        ["1", "2", "3"],               # All numeric
        ["one", "two", "-123", "1.5"], # No positive integers (Note: -123 and 1.5 are NOT digits)
        []                             # Empty
    ]
    for i, lst in enumerate(test_cases, 1):
        tup = tuple(lst)
        count = dem_phan_tu_dang_so(tup)
        print(f"Test {i}: {lst} -> Count: {count}")

if __name__ == "__main__":
    main()
    run_test_cases()