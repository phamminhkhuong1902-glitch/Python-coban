while True:
    try:
        N=int(input("Nhập n:"))
        if (N>0):
            break
    except ValueError:
        print ("Lỗi kiểu dữ liệu")

print ("---CÂU 1---") 
for i in range(1,N+1):
    if i%2==0:
        print (i,end=" ")
print()
print ("---CÂU 2---") 
tong=0
for i in range(1,N+1):
    if i%2!=0:
        tong+=i
print (f"Tổng số lẻ 1 đến n:{tong}") 
print ("---CÂU 3---") 
dem=0
for i in range(1,N+1):
    if i%3==0:
        dem+=1
print (f"Đếm các số chia hết cho 3 đến n:{dem}") 

print ("---CÂU 4---")
i=1
dem=0
while(i<=10):
    try:
        so=int(input(f"Nhập số thứ {i}:"))
        i+=1
        if(so<0):
            dem+=1
    except ValueError:
        print ("Lỗi kiểu dữ liệu")

print (f"Có {dem} số âm trong 10 số")

print ("---CÂU 5---")

n=int(input("Nhập n:"))
print (f"Bảng cửu chương {n}")
for i in range(1,11):
    print(f"{n} x {i} ={n*i}")

print ("---CÂU 6---")
for i in range(1,N+1):
    if i==5:
        continue
    print(i,end=" ")

print ("---CÂU 6---")
max=-1000
min=1000
i=1
while(i<=n):
    try:
        x=int(input(f"Nhập số thứ {i}:"))
        i+=1
        if x > max:
            max=x
        if x < min:
            min=x
    except:
        print ("Lỗi kiểu dữ liệu")
print(f"Số lớn nhất:{max}")
print(f"Số nhỏ nhất:{min}")
print ("---CÂU 8---")
while(i<=n):
    try:
        x=int(input(f"Nhập số thứ {i}:"))
        i+=1
        if x > max:
            max=x
        if x < min:
            min=x
    except:
        print ("Lỗi kiểu dữ liệu")
print(f"Số lớn nhất:{max}")
print(f"Số nhỏ nhất:{min}")
print ("---CÂU 9---")
so=int(input(f"Nhập số:"))
dem=0
so1=so
while(so!=0):
    so=so//10
    dem+=1
print(f"Số {so1} có {dem} chữ số")