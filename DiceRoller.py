from random import random


def roll(max):
    roll = int(random()*(max-1)+1)
    return roll


def four_sided_die():
    die_roll = roll(4)
    print(die_roll)


def six_sided_die():
    die_roll = roll(6)
    print(die_roll)


def eight_sided_die():
    die_roll = roll(8)
    print(die_roll)


def ten_sided_die():
    die_roll = roll(10)
    print(die_roll)


def twelve_sided_die():
    die_roll = roll(12)
    print(die_roll)


def twenty_sided_die():
    die_roll = roll(20)
    print(die_roll)


def hundred_sided_die():
    die_roll = roll(100)
    print(die_roll)


def input_input(prompt, choices):
    print(prompt)
    choice_number = 1
    for choice in choices:
        print(str(choice_number)+". " + choice)
        choice_number = choice_number+1
    while True:
        try:
            player_choice = int(input("> "))
            if player_choice >= 1 and player_choice <= len(choices):
                return player_choice-1
            else:
                print("Pick better number")
        except ValueError:
            print("invalid number lul")


print("Welcome to die roller")
diechoice = input_input("What die do you wish to roll?", ["4 sided", "6 sided", "8 sided", "10 sided", "12 sided", "20 sided", "100 sided"])
if diechoice == 0:
    four_sided_die()
elif diechoice == 1:
    six_sided_die()
elif diechoice == 2:
    eight_sided_die()
elif diechoice == 3:
    ten_sided_die()
elif diechoice == 4:
    twelve_sided_die()
elif diechoice == 5:
    twenty_sided_die()
elif diechoice == 6:
    hundred_sided_die()
