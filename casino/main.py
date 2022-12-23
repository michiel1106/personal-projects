from random import *
import time
import json
money = 2

randnum = random("red", "black", "green")
print(randnum)

# with open('data.json', 'w') as f:
# json.dump(money, f)

with open("data.json", "r") as f:
    data = json.load(f)

money = data["money"]

print("do you want to enable debug mode? Y/N")
debug_mode = input(">").lower()

if debug_mode == "y":
    debug_on = "on"
else:
    debug_on = "off"

print(f"""
welcome to my casino! 
You have {money} dollars please select what you want
1. Roulette
2. Red or Black (green coming to the future too)
3. even or uneven
4. 
5. 
6. debug
7. Reset money
""")

casino_choice = input(">")



if casino_choice == "1":
    roulette_random_number = randint(1, 37)
    if debug_on == "on":
        print(f"the number is: {roulette_random_number}")
    print("so you have chosen roulette! choose a number to set your money on, and how much")



    amount_number_roulette = input("what number (between 0 and 37: ")
    # the number they choose
    if int(amount_number_roulette) > 37:
        print("insufficient number! please choose anything between 0 and 37!")
    # amount of money
    amount_money_roulette = input(f"please choose how much money, you have {money} dollars if the number falls on what you guessed, it gets x5: ")
    # checks if the user inputted the correct numbers
    if int(amount_money_roulette) > money:
        print("insufficient funds!")
    else:
        print("betting successful!")

    if roulette_random_number == int(amount_number_roulette):
        money *= 5

with open('data.json', 'w') as f:
    json.dump({"money": money}, f)


if casino_choice == "2":
    print("ah, red or black, remember. it can be green too!")
    print(f"so, you have {money} dollars, what would you like to bet on. red, black, or green.")
    r_or_b = input(">")
    random_number = randint(1, 100)

    red_chance = 49
    black = 49
    green = 2
    # Choose a color based on the random number and the chances
    if 0 <= random_number <= red_chance:
        color = "red"
    elif random_number < red_chance:
        color = "black"























print(f"Your money is {money} now!")




