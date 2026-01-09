import os

# Đề bài: Viết hàm tinh_trung_binh(*args) nhận vào một lượng số bất kỳ.
# Hàm trả về giá trị trung bình cộng của các số đó. Nếu không có tham số nào được truyền vào, trả về 0.
def tinh_trung_binh(*args):
    sl =len(args)
    if sl == 0:
        return 0
    else:
        n = 0
        for i in args:
            n+=i
        return n / sl
def tinh_trung_binh_mau(*args):
    # args là một tuple chứa các tham số
    if not args:
        return 0
    return sum(args) / len(args)

# Đề bài: Viết hàm loc_du_lieu(*args) nhận vào hỗn hợp các kiểu dữ liệu (số nguyên, chuỗi, số thực...). 
# Hàm hãy lọc và trả về một list chỉ chứa các số nguyên (int) và bình phương chúng lên.
def loc_du_lieu(*args):
    list_moi = []
    for i in args:
        if isinstance(i,int) :
            list_moi.append(i**2)
    return list_moi
#    Đề bài: (Merge K Sorted Lists Simplified)Viết hàm merge_sorted_arrays(*args) nhận vào N
#    danh sách (list) số nguyên. Biết rằng mỗi danh sách đầu vào đã được sắp xếp tăng dần. 
#    Hãy gộp tất cả chúng lại thành một danh sách duy nhất cũng được sắp xếp tăng dần mà không dùng hàm sort() 
#    của Python (để luyện tư duy thuật toán).
#    Ví dụ: merge_sorted_arrays([1, 4, 5], [1, 3, 4], [2, 6]) -> [1, 1, 2, 3, 4, 4, 5, 6]
import heapq
def merge_sorted_arrays(*args):
    new_list = []
    for index_item, item_list in enumerate(args):
        if item_list:
            heapq.heappush(new_list,(item_list[0],index_item,0))
        result = []
    while new_list:
        value,list_index, item_index = heapq.heappop(new_list)
        result.append(value)
        # Nếu list vừa lấy ra vẫn còn phần tử tiếp theo, đẩy vào heap
        if item_index + 1 < len(args[list_index]):
            next_val = args[list_index][item_index + 1]
            heapq.heappush(new_list, (next_val, list_index,item_index + 1))
    return result




if __name__ == "__main__":
    kq = tinh_trung_binh(2,3,4,5,6)
    print(f"ket qua la {kq}")
    # Test
    print(tinh_trung_binh_mau(1, 2, 3))       # Output: 2.0
    print(tinh_trung_binh_mau(10, 20, 30, 40)) # Output: 25.0
    
    text = (1,2,5,2.3,"tungtung")
    lis = loc_du_lieu(*text)
    print(lis)
    # hoac print(loc_du_lieu(1, "hello", 2.5, 3, [1,2], 5))
    os.system('cls')
    print(merge_sorted_arrays([1, 4, 5], [1, 3, 4], [2, 6]))

