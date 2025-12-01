import uc_bc
while True:
        try:
            A=int(input("Nhập a:"))
            B=int(input("Nhập b:"))
            if A>0 and B>0:
                break
        except ValueError:
            print ("Lỗi nhập liệu")

print (f"Ước chung lớn nhất của {A} và {B}:{uc_bc.UCLN(A,B)}")