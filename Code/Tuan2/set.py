n = int(input("Nhap so luong tem hien co: "))
stamps_set = set()
dictionary_luuKQ = {}

for _ in range(n):
    country_name = input().strip()
    stamps_set.add(country_name)
    dictionary_luuKQ[country_name] = len(stamps_set)

# Sắp xếp theo giá trị (Value) tăng dần
# x là key, dictionary_luuKQ[x] là giá trị để mang đi so sánh
sorted_keys = sorted(dictionary_luuKQ, key=lambda x: dictionary_luuKQ[x])

# In kết quả theo thứ tự đã sắp xếp
print("\nKet qua sau khi sap xep theo thu tu ghi nhan:")
for key in sorted_keys:
    print(f"{key}: {dictionary_luuKQ[key]}")