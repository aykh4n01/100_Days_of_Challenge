print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height > 120:
    print("You can ride the rollecoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("You will need to pay child price, which is 3$")
    elif age <= 18:
        print("You will need to pay half price, which is 5$") 
    else:
        print("You will need to pay full price, which is 10$")
else:
    print("Sorry, you have to grow taller before you can ride.")
