print("Welcome to tip calculator!")

total_bill = float(input("What was the total bill?\n"))

tip = int(input("What percentage would you like to tip? 10, 12, 15?\n"))

num_people = int(input("How many people to split the bill?\n"))

bill_with_tip = total_bill + (total_bill * (tip / 100))

final_amount = bill_with_tip / num_people

print(round(final_amount, 2))