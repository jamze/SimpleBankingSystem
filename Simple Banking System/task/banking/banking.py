import random
import sqlite3

create_table_sql = ("CREATE TABLE IF NOT EXISTS card ("
                "id INTEGER primary key autoincrement, "
                "number TEXT, "
                "pin TEXT,"
                "balance INTEGER DEFAULT 0);")

insert_table_sql = '''INSERT INTO card (id, number, pin, balance) VALUES (Null,?,?,?);'''

get_all_sql = 'SELECT * FROM card'

get_number_sql = 'SELECT number FROM card WHERE number = ?;'

get_pin_sql = 'SELECT pin FROM card WHERE number = ?;'

get_balance_sql = "SELECT balance FROM card WHERE number=?;"

update_balance_sql = 'UPDATE card SET balance = ? WHERE number = ?'


def connect():
    return sqlite3.connect('card.s3db')

# c = connect().cursor()

def create_tables(cursor):
    # with cursor:
        return cursor.execute(create_table_sql)

def add_value(cursor, number, pin, balance):
    with cursor:
        cursor.execute(insert_table_sql, (number, pin, balance))

def get_all(cursor):
    with cursor:
        return cursor.execute("SELECT * FROM card;").fetchall()

def get_number(cursor, number):
    with cursor:
        return cursor.execute(get_number_sql, (number,)).fetchall()

def get_pin(cursor, number):
    with cursor:
        return cursor.execute(get_pin_sql, (number,)).fetchall()


connection = connect()
cursor = connection.cursor()
create_tables(cursor)


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
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
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

        # id = 1
        number = user1.number
        pin = user1.pin
        balance = random.randrange(0, 99)

        add_value(connection, number, pin, balance)
        connection.commit()

    elif value == 2:
        log_into(user1)

    elif value == 3:
        cursor.execute("DELETE FROM card")

    elif value == 4:
        cursor.execute("DROP TABLE card")

    # elif value == 3:
    #     cards = connection.execute("SELECT * FROM card;").fetchall()
    #
    #     for card in cards:
    #         print(card)

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

    if contr_num == 10:
        contr_num = 0
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
    # return "1"

def create_pin():
    pin = []
    for y in range(0, 4):
        pin.insert(y, random.randrange(0, 9))

    return (''.join(str(elem) for elem in pin))
    # return "1"

def log_into(user):
    print("\nEnter your card number")
    card_input = input()
    print("Enter your PIN")
    pin_input = input()

    cursor.execute(get_pin_sql, (card_input,))

    pin_card = (cursor.fetchone())
    if pin_card:
        if pin_input == pin_card[0]:
            print('Match')
            print("\nYou have successfully logged in!")
            program_log(card_input)

    #     if card_input == user.number and pin_input == user.pin:
    #         print("\nYou have successfully logged in!")

        else:
            print("Wrong card number or PIN!")

def program_log(card_input):
    while True:
        menu_log()
        value = int(input())
        if value == 0:
            print("\nBye!")
            exit()

        elif value == 1:
            # print("\nBalance")
            # print(get_all(connection))        #debug
            cursor.execute(get_balance_sql, (card_input,))
            print("Balance:", cursor.fetchone()[0])

        elif value == 2:
            print("\nEnter income:")
            income = int(input())

            cursor.execute(get_balance_sql, (card_input,))
            curr_balance = cursor.fetchone()[0]
            new_balance = income + curr_balance

            cursor.execute(update_balance_sql, (new_balance, card_input,))

            print("Income was added!")

        elif value == 3:
            print("Transfer")
            print("Enter card number:")

            trans_number = input()

            if len(trans_number) != 16:
                "not proper length"

            # print(trans_number[:15])
            # print(Luhn_alg(trans_number[:15]))
            # print(trans_number[15])

            if int(Luhn_alg(trans_number[:15])) != int(trans_number[15]):
                print("Such a card does not exist.")

            print("Enter how much money you want to transfer")
            trans_money = int(input())

            cursor.execute(get_balance_sql, (card_input,))
            curr_balance = cursor.fetchone()[0]

            if curr_balance < trans_money:
                print("Not enough money!")
            else:

                new_balance = curr_balance - trans_money

                cursor.execute(update_balance_sql, (new_balance, card_input,))

                cursor.execute(get_balance_sql, (trans_number,))
                curr_balance = cursor.fetchone()[0]
                new_balance = curr_balance + trans_money

                cursor.execute(update_balance_sql, (new_balance, trans_number,))

                cursor.execute(get_balance_sql, (trans_number,))
                print("Balance on second account:", cursor.fetchone()[0])
















        elif value == 5:
            print("\nYou have successfully logged out!")
            break

        else:
            print("Invalid")



while True:
    main()

