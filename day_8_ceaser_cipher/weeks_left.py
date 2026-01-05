age = int(input("Enter your age: "))
def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52
    hours_left = years_left * 365 * 24
    print(f"You have {weeks_left} weeks left and {hours_left} hours left to live.")

life_in_weeks(age)