import random

class User:
    def __init__(self, number, pin):
        self.number = number
        self.pin = pin
        self.balance = None

        def operation(self, money):
            self.balance = money

def menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")


def menu_log():
    print("\n1. Balance")
    print("2. Log out")
    print("0. Exit")


def main():
    menu()
    value = int(input())

    if value == 0:
        print("\nBye!")
        exit()

    elif value == 1:
        global user1
        user1 = User(create_account(), create_pin())

        print("\nYour card has been created")
        print("Your card number:")
        print(user1.number)
        print("Your card PIN:")
        print(user1.pin)
        print("")

    elif value == 2:
        log_into(user1)
    else:
        print("Invalid")


def Luhn_alg(card_number):
    i = 0
    Luhn_sum = 0

    for num in card_number:
        i += 1
        if i % 2 != 0:
            num = int(num) * 2

        if int(num) > 9:
            num = int(num) - 9

        Luhn_sum += int(num)

    contr_num = 10 - (Luhn_sum % 10)
    return contr_num


def create_account():
    card_number = []
    card_number.insert(0, 4)
    for i in range(1, 6):
        card_number.insert(i, 0)
    for i in range(6, 15):
        card_number.insert(i, random.randrange(0, 9))

    card_number.insert(15, Luhn_alg(card_number))

    return (''.join(str(elem) for elem in card_number))


def create_pin():
    pin = []
    for y in range(0, 4):
        pin.insert(y, random.randrange(0, 9))

    return (''.join(str(elem) for elem in pin))


def log_into(user):
    print("\nEnter your card number")
    card_input = input()
    print("Enter your PIN")
    pin_input = input()

    if card_input == user.number and pin_input == user.pin:
        print("\nYou have successfully logged in!")
        program_log()

    else:
        print("Wrong card number or PIN!")
        # return 0


def program_log():
    while True:
        menu_log()
        value = int(input())
        if value == 0:
            print("\nBye!")
            exit()

        elif value == 1:
            print("\nBalance")
            print(0)

        elif value == 2:
            print("\nYou have successfully logged out!")
            break

        else:
            print("Invalid")


while True:
    main()
