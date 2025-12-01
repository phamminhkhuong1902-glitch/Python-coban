import hcn
try:
    cd=float(input("Nhập chiều dài:"))
    cr=float(input("Nhập chiều rộng:"))
except ValueError:
    print ("Sai kiểu dữ liệu")
else:
    cvdt=hcn.tinhcvdt(cd,cr)
    print (f"Chu vi: {cvdt[0]}")
    print (f"Diện tích: {cvdt[1]}")
    print (f"Diện tích  {cvdt[0]} và diện tích {cvdt[1]}")