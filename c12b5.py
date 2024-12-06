print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

# Sắp xếp theo chiều cao, rồi theo ID (sử dụng lexsort)
# lexsort yêu cầu các tham số sắp xếp theo thứ tự: thứ tự sắp xếp chiều cao trước rồi tới ID
indices = np.lexsort((student_id, student_height))

# In các chỉ số nguyên mô tả thứ tự sắp xếp
print("Chỉ số:")
print(indices)

# In dữ liệu đã sắp xếp theo thứ tự
print("Dữ liệu sắp xếp:")
for idx in indices:
    print(student_id[idx], student_height[idx])
