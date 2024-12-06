print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import datetime as dt

# Định dạng ngày giờ
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển chuỗi thành đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In ra ngày, tháng, phút, giây của đối tượng t1
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))

# Lấy ngày và giờ hiện tại
t2 = dt.datetime.now()

# Tính toán sự chênh lệch giữa hai thời điểm
diff = t2 - t1

# In ra số ngày chênh lệch
print('How many days difference? ' + str(diff.days))
