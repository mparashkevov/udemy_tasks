from random import randint
dice_num = ["1","2","3","4","5","6"]
dice_roll = randint(0,5)
print(dice_num[dice_roll])

year = int(input("Whar year are you born in: "))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)