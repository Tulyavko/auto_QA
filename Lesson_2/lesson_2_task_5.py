def month_to_season(n):
    if n in range(1, 12):
        if n in range(1, 2) or n == 12:
            print("Winter")
        elif n in range(3, 5):
            print("Spring")
        elif n in range(6, 8):
            print("Summer")
        else:
            print("Autumn")
    else: 
        print("Неверное число!!!")
month_to_season(14)