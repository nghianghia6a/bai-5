print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import numpy as np

# Định nghĩa kiểu dữ liệu và tạo mảng có cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]
students = np.array(students_details, dtype=data_type)

# In mảng gốc và mảng sắp xếp theo chiều cao
print("Original array:")
print(students)
print("\nSort by height:")
print(np.sort(students, order='height'))
