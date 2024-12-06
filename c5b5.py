print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Chương trình chính (cả module và chương trình chính trong một tệp)

# Hàm tìm phần tử lớn nhất trong danh sách
def find_max(lst):
    return max(lst)

# Hàm tìm phần tử nhỏ nhất trong danh sách
def find_min(lst):
    return min(lst)

# Hàm sắp xếp danh sách
def sort_list(lst):
    return sorted(lst)

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các phần tử vào danh sách
lst = []
print("Nhập các phần tử trong danh sách:")
for i in range(n):
    lst.append(int(input(f"Phần tử {i+1}: ")))

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = find_max(lst)
min_value = find_min(lst)

# Sắp xếp danh sách
sorted_lst = sort_list(lst)

# In kết quả
print("Danh sách đã sắp xếp:", sorted_lst)
print("Phần tử lớn nhất trong danh sách:", max_value)
print("Phần tử nhỏ nhất trong danh sách:", min_value)
