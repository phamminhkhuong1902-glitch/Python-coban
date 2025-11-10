import math
a=float(input("Nhập A: "))
b=float(input("Nhập B: "))
c=float(input("Nhập C: "))
delta=b**2-(4*a*c)
if delta<0:
    print("Vô nghiệm")
elif delta==0:
    x=-b/(2*a)
    print(f"x= {x}")
else :
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b-math.sqrt(delta))/2*a
    print(f"x1= {x1} x2={x2}")
