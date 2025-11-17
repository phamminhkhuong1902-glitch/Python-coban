try:
    van=float(input("Nhập điểm môn Van:"))
    toan=float(input("Nhập điểm môn Toan:"))
    anh=float(input("Nhập điểm môn Anh:"))
except ValueError:
    print ("Nhập sai kiểu dữ liệu")
else:
    dtb=(van+toan+anh)/3
    if(van<0 or van>10 or toan<0 or toan>10 or anh<0 or anh>10):
        print ("Lỗi nhập sai giá trị")
    else:  
        if(dtb>=9):
            print ("Xuất sắc")
        elif(dtb>=8):
            print ("Giỏi")
        elif(dtb>=7):
            print ("Khá")
        elif(dtb>=5):
            print ("Trung bình")
        else:
            print ("Yếu")