import math
km = int(input('Nhập số km: '))
tien = 0

if km < 1:
    print ('Quảng đường đi không hợp lệ')
elif km  == 1:
    tien = 20000 
    print(f"Tiền taxi:{tien}") 
elif km <= 5:
    tien = 20000 + (km - 1) * 16000
    print(f"Tiền taxi:{tien}") 
elif km <= 10:
    tien = 20000 + 4 * 16000 + (km - 5) * 13000
    print(f"Tiền taxi:{tien}") 
else:
    tien = 20000 + 4 * 16000 + 5 * 13000 + (km - 10) * 10000
    print(f"Tiền taxi:{tien}") 

if tien > 200000:
    tien = tien *0.9
    print(f"Tiền taxi:{tien}")