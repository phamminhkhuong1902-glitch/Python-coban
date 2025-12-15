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