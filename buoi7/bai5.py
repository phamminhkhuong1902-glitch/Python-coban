
def nhapsogio():
    while True:
        try:
            h=float(input("Nhập số giờ:"))
            if(h>0):
                return h
        except ValueError:
            print ("Lỗi kiểu dữ liệu")
import math
def tientaxi(h):
    tien=0 
    gio=math.ceil(h)
    if gio<=2:
        tien=gio*5000
    elif gio<=6:
        tien=2*5000+(gio-3)*4000
    else :
        tien=2*5000+4*4000+(gio-6)*3000
    return tien
h=nhapsogio()
tongtien=tientaxi(h)
print(f"Số giờ đi:{math.ceil(h)}")
print(f"Tiển taxi:{int(tongtien)}")
