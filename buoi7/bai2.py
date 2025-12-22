Tuoi=[12,15,14,18,16,13,20,17,11]
def tuoitrungbinh(Tuoi):
    tong=0
    for value in Tuoi:
        tong+=value
    return tong/len(Tuoi)

def tuoinhonhat(Tuoi):
    Min=Tuoi[0]
    for value in Tuoi:
        if(value < Min):
            Min=value
    return Min

def demtuoi(Tuoi):
    nho=0
    lon=0
    for value in Tuoi:
        if value >=16:
            lon+=1
        else:
            nho+=1
    return lon,nho
tuoitb=int(tuoitrungbinh(Tuoi))
demtuoi16=demtuoi(Tuoi)        
print (f"Tuổi trung bình :{tuoitb}")
print(f"Tuổi nhỏ nhất:{tuoinhonhat(Tuoi)}")
print(f"Số tuổi đủ 16 :{demtuoi16[0]}")
print(f"Số tuổi dưới 16 :{demtuoi16[1]}")