# This calculate how many days, weeks, months and years left till 90 years old
age = input("What is your current age?")

age_as_int = int(age)
year_remaining = 90 - age_as_int
days_remaining = 365 * year_remaining
weeks_remaining = 52 * year_remaining
month_remaining = 12 * year_remaining

print(f"You have {days_remaining} days, {weeks_remaining} weeks, {month_remaining} month and {year_remaining} years remainig")