import math
a=float(input("Nhập A: "))
b=float(input("Nhập B: "))
c=float(input("Nhập C: "))
if(a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b):
    cv=a+b+c
    p=cv/2
    dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Chu vi={cv} Diện tích={dt}")
else:
    print("Không phải tam giác")