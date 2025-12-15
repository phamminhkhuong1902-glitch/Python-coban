Nhietdo=[30,28,35,33,29,31,27,34]
def nhietdotrungbinh(nhietdo):
    tong=0
    for value in Nhietdo:
        tong+=value
    return tong/len(Nhietdo)

def nhietdolonnhat(Nhietdo):
    Max=Nhietdo[0]
    for value in Nhietdo:
        if(value < Max):
            Max=value
    return Max

def demnhietdonong(Nhietdo):
    nho=0
    lon=0
    for value in Nhietdo:
        if value >=32:
            lon+=1
        else:
            nho+=1
    return lon,nho
ndtb=int(nhietdotrungbinh(Nhietdo))
demnhietdo=demnhietdonong(Nhietdo)        
print (f"Nhiệt độ trung bình :{ndtb}")
print(f"Nhiệt độ lớn nhất:{nhietdolonnhat(Nhietdo)}")
print(f"Số ngày nóng :{demnhietdo[0]}")
print(f"Số ngày không nóng :{demnhietdo[1]}")