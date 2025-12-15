import random
print ("--Câu--1")
Diem=[7.5,8.0,6.0,9.0,5.5,8.5,7.0,6.5]
def diemtrungbinh(Diem):
    tong=0
    for value in Diem:
        tong+=value
    return tong/len(Diem)

def diemcaonhat(Diem):
    Max=Diem[0]
    for value in Diem:
        if(value > Max):
            Max=value
    return Max
def demdiem(Diem):
    nho=0
    lon=0
    for value in Diem:
        if value >=8.0:
            lon+=1
        else:
            nho+=1
    return lon,nho

demdiem8=demdiem(Diem)        
print (f"Điểm trung bình :{diemtrungbinh(Diem)}")
print(f"Điểm cao nhất:{diemcaonhat(Diem)}")
print(f"Số điểm từ 8 :{demdiem8[0]}")
print(f"Số điểm dưới 8 :{demdiem8[1]}")

for i in range(len(Diem)-1):
    for j in range(i+1,len(Diem)):
        if(Diem[i] > Diem[j]):
            Diem[i],Diem[j]=Diem[j],Diem[i]

print (f"Sắp xếp tăng dần:{Diem}")
print("--Câu 2--")
while True:
    try:
        x=float(input("Nhập số m nước:"))
        if x>=0:
            break
    except ValueError:
        print ("Nhập sai kiểu dư liệu")

    tiennuoc=0
    if x<=10:
        tiennuoc=x*7000
    elif x<=20:
        tiennuoc=7000*10+(x-10)*9000

tiennuoc=7000*10+9000*10+(x-20)*12000
phi=tiennuoc*0.05
tongtien=int(tiennuoc+phi)
print (f"Tổng tiền nước: {tongtien}")
print("--Câu 3--")
diem=0
for i in range(1,7):
    print("Lượt",i)
    if random.random()<0.6:
        diemcong=random.randint(5,30)
        diem+=diemcong
        print("Tìm thấy kho báu ")
        print (f"cộng {diemcong} điểm")
    else:
        diem=diem-2
        
        if(diem<=0):
            diem=0
            print("Không tìm thấy trừ 2 điểm")
    print(f"Tổng điểm:{diem}")
    if diem>=80:
        print("Thắng")
if(diem<80):
    print("Thua")

