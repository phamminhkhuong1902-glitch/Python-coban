import kt_ham

print("Nhập N để in tam giác")
n = kt_ham.NhapN()

kt_ham.xuat(n)

print("Nhập số để kiểm tra số hoàn hảo")
So = kt_ham.NhapN()

if kt_ham.sohh(So):
    print(f"Số {So} là số hoàn hảo")
else:
    print(f"Số {So} không là số hoàn hảo")
