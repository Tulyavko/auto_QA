def bank(x,y):
    for i in range(1, y + 1):
        x = x * 1.1
    print(round(x, 2))
bank(100, 10)