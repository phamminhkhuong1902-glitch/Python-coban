try:
    a=int(input("Nhập số: "))
except:
    print("Lỗi nhập liệu")
else:    
    if(a%2==0):
        print(f"{a} là số chẵn")
    else:
        print(f"{a} là số lẻ")
