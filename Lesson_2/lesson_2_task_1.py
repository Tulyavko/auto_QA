lst = ["виноград", "персик", "груша", "апельсин", "банан", "яблоко"]
for i in range(0, len(lst)):
    if (i == 0) or (i == len(lst)-1):
        print(lst[i])