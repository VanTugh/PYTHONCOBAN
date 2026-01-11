# Cach 1
# n, m = map(int, input().split())

# arr = list(map(int, input().split()))
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))

# happiness = 0
# for i in arr:
#     if i in A:
#         happiness +=1
#     if i in B:
#         happiness -=1
# print(happiness)
import sys
def solve():
    # Doc toan bo du lieu mot lan de tang toc do (thay vi input() nhieu lan)
    input_data = sys.stdin.read().split()
    
    # n = input_data[0], m = input_data[1]
    # Mang chinh tu vi tri 2 den n+2
    n, m = map(int, input_data[:2])
    arr = input_data[2 : n+2]
    
    # Set A va Set B (dung set de lookup O(1))
    A = set(input_data[n+2 : n+m+2])
    B = set(input_data[n+m+2 : n+2*m+2])
    
    # Cach viet toi uu va cuc nhanh trong Python:
    # (i in A) tra ve True (1) hoac False (0)
    happiness = sum((i in A) - (i in B) for i in arr)
    
    print(happiness)

if __name__ == '__main__':
    solve()