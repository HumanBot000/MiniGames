import os
import random
import re
import time

from colorama import Fore


def get_coins():
    settings_file = open("settings.txt", "r+")
    coins = settings_file.readlines()[0]
    coins = int(re.split(":", coins)[1])
    return coins


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def update_coins(coins):
    settings_file = open("settings.txt", "r+").readlines()
    os.remove("settings.txt")
    f = open('settings.txt', 'a')
    f.write(f"money:{coins}\n")


def settings(coins):
    print(Fore.RESET)
    clear_console()
    print(Fore.BLUE)
    try:
        setting = int(input("Please select a setting:   [1] Give Coins | [2] Remove Coins | [3] Exit:"))
    except Exception:
        print(Fore.RED)
        print("Please enter a valid  number")
        settings()

    if setting == 1:
        try:
            coins_to_give = int(input("How much Coins do you want to cheat? Please enter the amount:"))
        except Exception:
            print(Fore.RED)
            print("Please enter a number")
            settings(coins)
        coins = coins + coins_to_give
        update_coins(coins)
    if setting == 2:
        try:
            coins_to_clear = int(input("How much Coins do you want to remove? Please enter the amount:"))
        except Exception:
            print(Fore.RED)
            print("Please enter a number")
            settings(coins)
        coins = coins - coins_to_clear
        update_coins(coins)

    if setting == 3:
        main()
    print(Fore.RESET)
    settings(coins)


def game_black_jack():
    clear_console()
    print(Fore.RESET)
    print(Fore.CYAN)
    try:
        game = int(input("Please select a Task:    [0] Rules | [1] Play  | [2] Back:"))
    except Exception:
        print(Fore.RED)
        print("Please enter a valid number")
        game_black_jack()
    if game == 1:
        coins = get_coins()
        print(Fore.YELLOW)
        try:
            bet = int(input("How much do you bet?:"))
            if coins < bet:
                print(Fore.RED)
                print(f"You only have {coins} coins")
                print(Fore.RESET)
                game_black_jack()
        except Exception:
            print(Fore.RED)
            print("Please enter a valid number")
            game_black_jack()
        coins = coins - bet
        own_amount = 0
        while True:
            print(Fore.MAGENTA)
            try:
                option = int(input(
                    f"The Maximum is 20,you have {own_amount} what do you like to do? [0] Reveal Dealers Score | [1] Raise Score:"))
            except Exception:
                print(Fore.RED)
                print("Please enter a valid number")
            else:
                if option == 0:
                    dealer_amount = random.randint(15, 20)
                    if own_amount == dealer_amount:
                        print(Fore.YELLOW)
                        print("Its a tie you get your coins back")
                        print(Fore.RESET)
                        coins = coins + bet
                        update_coins(coins)
                        time.sleep(3)
                        game_black_jack()
                    elif own_amount > dealer_amount:
                        print(Fore.GREEN)
                        print(f"You won the dealer had {dealer_amount} points your coins will be multiply by 2x")
                        print(f"now you have {coins + bet + bet} coins")
                        print(Fore.RESET)
                        coins = coins + bet + bet
                        update_coins(coins)
                        time.sleep(3)
                        game_black_jack()
                    elif own_amount < dealer_amount:
                        print(Fore.RED)
                        print(f"You loosed the dealer had {dealer_amount} points your coins are gone")
                        print(Fore.RESET)
                        update_coins(coins)
                        time.sleep(3)
                        game_black_jack()
                if option == 1:
                    own_amount = own_amount + random.randint(1, 5)
                    if own_amount > 20:
                        print(Fore.RED)
                        print(f"You Lose your score is now {own_amount} your points are gone")
                        print(Fore.RESET)
                        update_coins(coins)
                        time.sleep(3)
                        game_black_jack()
    if game == 1:
        pass
    if game == 2:
        get_game()


def get_game():
    clear_console()
    print(Fore.RESET)
    print(Fore.CYAN)
    try:
        game = int(input("Please select a game:     [0] Guess the Number | [1] Black Jack | [2] Back:"))
    except Exception:
        print(Fore.RED)
        print("Please enter a valid number")
        get_game()
    if game == 0:
        pass
    if game == 1:
        game_black_jack()
    if game == 2:
        main()


def main():
    coins = get_coins()
    print(Fore.RESET)
    print(Fore.RED)
    print(f"You have {coins} coins.")
    print(Fore.GREEN)
    try:
        game = int(input("Please select a task:     [0] Help | [1] Settings | [2] Games:"))
    except Exception:
        print(Fore.RED)
        print("Please enter a valid number")
        game = 0
    print(Fore.RESET)
    if game == 0:
        clear_console()
        print(Fore.CYAN)
        print("""Actions: You have to enter the number in the brackets([ and ]) before the Action
            Economy:You have an specific balance on your bank you will see it at the main screen.If you win in games you will multiple your money.If you haven´t enough money you can cheat some in the settings
        """)
        main()
    if game == 1:
        settings(coins)
    if game == 2:
        get_game()


main()
