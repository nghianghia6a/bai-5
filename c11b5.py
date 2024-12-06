print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import numpy as np

# Dữ liệu đầu vào
data = np.array([('James', 5, 48.5), 
                 ('Nail', 6, 52.5), 
                 ('Paul', 5, 42.1), 
                 ('Pit', 5, 40.11)],
                dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])

# Sắp xếp mảng theo 'class' và sau đó 'height'
sorted_data = np.sort(data, order=['class', 'height'])

# In kết quả sau sắp xếp
print("Kết quả sắp xếp:")
for entry in sorted_data:
    print(entry)
