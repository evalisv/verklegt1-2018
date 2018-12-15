from datetime import date

# dagurinn = str(date.today()).split("-")
# year, month, day = dagurinn

# print(year, month, day)
day_of_return = str(date.today().strftime("%d.%m.%Y"))
print(day_of_return)