print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import numpy as np

# Tạo mảng với các giá trị từ 12 đến 38 (bao gồm 12 và không bao gồm 38)
x = np.arange(12, 38)

# In ra mảng ban đầu
print("Mảng được tạo:")
print(x)

# Đảo ngược mảng
x_reversed = x[::-1]

# In ra mảng sau khi đảo ngược
print("Mảng đảo ngược:")
print(x_reversed)
