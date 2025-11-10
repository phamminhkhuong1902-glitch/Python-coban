thang=int(input("Nhập tháng: "))
match thang:
    case 1|2|3:
        print("Mùa xuân")
    case 4|5|6:
        print("Mùa hạ")
    case 7|8|9:
        print("Mùa thu")
    case 10|11|12:
        print("Mùa đông")   
    case _:
        print("Nhập lại")