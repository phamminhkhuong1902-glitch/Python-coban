import random
def trochoi_ban_sung():
    tongdiem=0
    toida_phatban=7
    print ("---Trò chơi bắn mục tiêu---")
    for phat in range(1,toida_phatban+1):
        if random.random()<0.4:
            cong=random.randint(10,25)
            tongdiem+=cong
            print(f"Phát thứ {phat}:")
            print(f"Đã trúng cộng thêm {cong} điểm")
            print(f"Tổng điểm:{tongdiem}")
        else:
            tru=0
            tongdiem-=tru
            print(f"Đã trượt trừ {tru} điểm")
            print(f"Tổng điểm:{tongdiem}")
        if tongdiem>=90:
            print (f"Bạn đã thắng với tổng điểm {tongdiem}")
    if(tongdiem<90):
        print (f"Bạn đã thua với tổng điểm {tongdiem}")

trochoi_ban_sung()

def trochoi_nap_nangluong():
    tongdiem=0
    toida_nap=5
    print ("---Trò chơi nạp năng lượng---")
    for nap in range(1,toida_nap+1):
        if random.random()<0.5:
            cong=random.randint(15,40)
            tongdiem+=cong
            print(f"Nạp thứ {nap}:")
            print(f"Đã nạp thành công cộng thêm {cong} điểm")
            print(f"Tổng điểm:{tongdiem}")
        else:
            tru=random.randint(5,15)
            tongdiem-=tru
            print(f"Đã nạp thất bại trừ {tru} điểm")
            print(f"Tổng điểm:{tongdiem}")
        if tongdiem>=120:
            print (f"Bạn đã thắng với tổng điểm {tongdiem}")
    if(tongdiem<120):
        print (f"Bạn đã thua với tổng điểm {tongdiem}")
trochoi_nap_nangluong()

def trochoi_san_khobau():
    tongdiem=0
    toida_luot=6
    print ("---Trò chơi săn kho báu---")
    for luot in range(1,toida_luot+1):
        if random.random()<0.6:
            cong=random.randint(15,40)
            tongdiem+=cong
            print(f"Lượt thứ {luot}:")
            print(f"Đã  thành công cộng thêm {cong} điểm")
            print(f"Tổng điểm:{tongdiem}")
        else:
            tru=2
            tongdiem-=tru
            print(f"Đã  thất bại trừ {tru} điểm")
            print(f"Tổng điểm:{tongdiem}")
        if tongdiem>=120:
            print (f"Bạn đã thắng với tổng điểm {tongdiem}")
    if(tongdiem<120):
        print (f"Bạn đã thua với tổng điểm {tongdiem}")

trochoi_san_khobau()