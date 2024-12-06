print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

from utils import find_max_min  # Import module đã tạo

def main():
    # Nhập số lượng phần tử của danh sách
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    lst = []

    # Nhập giá trị cho danh sách
    for i in range(n):
        value = float(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
        lst.append(value)

    # Sử dụng module để tìm max, min và vị trí
    max_val, max_idx, min_val, min_idx = find_max_min(lst)

    # In kết quả
    print(f"Phần tử lớn nhất: {max_val} (vị trí: {max_idx + 1})")  # Vị trí +1 để tính từ 1
    print(f"Phần tử nhỏ nhất: {min_val} (vị trí: {min_idx + 1})")

if __name__ == "__main__":
    main()

