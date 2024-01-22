
import re
from sys import stdin

for line in stdin.readlines():
    s = re.split('\\s+', line.lower().strip())
    print(s)
    if re.match('^.*[\\.\\?\\!]$', s[-1]):
        if len(s[-1]) > 1:
            print(' '.join(s).capitalize())
        else:
            print(' '.join(s[:-1]).capitalize() + s[-1])
    else:
        print(' '.join(s).capitalize() + '.')


'''
Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.

co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin

muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep

moi    CAC BAN danG ky     thaM giA !
'''