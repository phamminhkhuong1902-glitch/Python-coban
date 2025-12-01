def tinhcv(cd,cr):
    cv=(cd+cr)*2
    return cv

def tinhdt(cd,cr):
    dt=cd*cr
    return dt

def tinhcvdt(cd,cr):
    cv=(cd+cr)*2
    dt=cd*cr
    return cv,dt
try:
    cd=float(input("Nhập chiều dài:"))
    cr=float(input("Nhập chiều rộng:"))
except ValueError:
    print ("Sai kiểu dữ liệu")
else:
    cvdt=tinhcvdt(cd,cr)
    print (f"Chu vi: {tinhcv(cd,cr)}")
    print (f"Diện tích: {tinhdt(cd,cr)}")
    print (f"Diện tích  {cvdt[0]} và diện tích {cvdt[1]}")