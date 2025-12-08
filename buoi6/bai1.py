print ("--CÂU 1--")
chuoi=str(input("Nhập chuỗi:"))
print ("Chiều dài chuỗi",len(chuoi))
print ("--CÂU 3--")
ktdau=chuoi[0:3]
ktcuoi=chuoi[2:]
print (f"3 ký tự đầu:{ktdau}")
print (f"3 ký tự cuối:{ktcuoi}")
print ("--CÂU 4--")
ten=str(input("Nhập tên:"))
print (ten)
print ("Tên viết hoa:",str.upper(ten))
print ("Tên viết thường:",str.lower(ten))
print ("--CÂU 5--")
Ho=str(input("Nhập họ:"))
Tendem=str(input("Nhập tên đệm:"))
Ten=str(input("Nhập tên:"))
hovaten="Họ tên là {}"
print(hovaten.format(Ho),(Tendem),(Ten))
print ("--CÂU 6--")
s=str(input("Nhập chuỗi:"))
kt=str(input("Kiểm ta có từ xuất hiện:"))
print(s.startswith(kt,0,30))
s1=str(input("Nhập chuỗi:"))
print(s1.replace("/","-"))
s2="        Khuong"
s3=(s2.strip(" "))
print(s3)


