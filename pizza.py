print("Welcome to the Pizza Shop!")

size = input("What size of pizza would you like? S, M, or L: ")
add_pepperoni = input("Would you like to add pepperoni? Y or N: ")
extra_cheese = input("Would you like to add extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 150
    if add_pepperoni == "Y":
        bill += 20
elif size == "M":
    bill += 200
    if add_pepperoni == "Y" or add_pepperoni == "N":
        bill += 30
elif size == "L":
    bill += 250
    if add_pepperoni == "Y" or add_pepperoni == "N":
        bill += 30

if extra_cheese == "Y":
    bill += 10

print(f"Your final bill is: Rs. {bill}. Enjoy your pizza!")

