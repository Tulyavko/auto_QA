def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
year_check = 2004
leap = is_year_leap(year_check)
print(f"год {year_check}: {leap}")