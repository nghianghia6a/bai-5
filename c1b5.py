print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# File: mymath.py

# Hàm tính bình phương của một số
def square(n):
    return n * n

# Hàm tính lập phương của một số
def cube(n):
    return n * n * n

# Hàm tính giá trị trung bình của một danh sách
def average(values):
    nvals = len(values)
    total_sum = 0.0
    for v in values:
        total_sum += v
    return float(total_sum) / nvals
