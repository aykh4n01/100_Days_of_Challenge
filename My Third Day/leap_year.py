year = int(input("Which year do you want to check?\n"))

if ((year % 4 == 0) and
    (year % 100 != 0) or
    (year % 400 == 0) and
    (year % 100 == 0)):
    print(f"{year} Leap Year!")
else:
    print(f"{year} is not leap Year!")