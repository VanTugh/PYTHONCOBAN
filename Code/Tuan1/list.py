from trenlop import xoa_man_hinh
# Câu hỏi: Viết một hàm nhận vào một list các số nguyên. 
# Hàm trả về một list mới chỉ chứa bình phương của các số chẵn, lập phương các số lẻ trong list ban đầu. 
# (Khuyến khích dùng List Comprehension).
a = [1,2,3,4,5,6,7,8,9]
b = [x ** 2 if x % 2 ==0 else x**3 for x in a ]
print(b)
# Câu 3: Mức độ Vận dụng cao (High Application) - LeetCode 53
# Câu hỏi (Maximum Subarray): Cho một mảng số nguyên nums. Hãy tìm một mảng con liên tiếp (subarray) có tổng lớn nhất và trả về tổng đó. 
# Yêu cầu: Độ phức tạp thời gian là O(n).
xoa_man_hinh()
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] Output: 6 (Mảng con là [4, -1, 2, 1])
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def Kadane(nums):
    nums_max = nums[0]
    max_curr = nums[0]
    for i in range(1, len(nums)):
        max_curr = max(nums[i], nums[i]+max_curr)
        nums_max = max(nums_max, max_curr)
    print(f"tong ket qua cua mang moi la : {nums_max}")
# Câu hỏi: Tích của mảng trừ chính nó (Product of Array Except Self) Cho một mảng số nguyên nums.
# Hãy trả về một mảng answer sao cho answer[i] bằng tích của tất cả các phần tử trong nums ngoại trừ nums[i].
# Yêu cầu khó:
# Thời gian chạy phải là O(n).
# KHÔNG được sử dụng phép chia (Division).
# (Vì nếu dùng phép chia, bạn chỉ cần tính tổng tích rồi chia cho từng số là xong, bài toán trở nên quá dễ).
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
input = [1,2,3,4,5]
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    
    # Bước 1: Tính tích các số bên TRÁI (Prefix Product)
    # answer[i] sẽ lưu tích các số từ nums[0] đến nums[i-1]
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
    
    # Bước 2: Tính tích các số bên PHẢI (Suffix Product) và nhân dồn vào answer
    # right_product lưu tích các số từ nums[i+1] đến cuối
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
        
    return answer

# Test
print(product_except_self(input))
# Output: [24, 12, 8, 6]