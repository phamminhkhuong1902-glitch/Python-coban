import math
try:
    thang=int(input("Nhập tháng:"))
except:
    print("Nhập lỗi")
else:
    match thang:
        case 1|3|5|7|8|10|12:
            print("Tháng có 31 ngày")
        case 4|6|9|11:
            print("Tháng có 30 ngày")
        case 2:
            print("Tháng có 28 hoặc 29 ngày")
        case _:
            print("Nhập không hợp lệ")