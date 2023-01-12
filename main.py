import os
import random
import re

from colorama import Fore


def disk_adjustsize(size):
    factor = 1024
    for i in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if size > factor:
            size = size / factor
        else:
            return f"{size:.3f}{i}"


def get_coins():
    settings_file = open("settings.txt", "r+")
    coins = settings_file.readlines()[0]
    coins = int(re.split(":", coins)[1])
    if coins <= 0:
        coins = 0
    return int(coins)


def get_version():
    settings_file = open("settings.txt", "r+")
    version = settings_file.readlines()[1]
    version = str(re.split(":", version)[1])
    return version


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def update_coins(coins):
    settings_file = open("settings.txt", "r+").readlines()
    os.remove("settings.txt")
    f = open('settings.txt', 'a')
    data = settings_file
    data[0] = f"money:{coins}\n"
    f.writelines(data)


def settings(coins):
    print(Fore.RESET)
    clear_console()
    print(Fore.BLUE)
    try:
        setting = int(input("Please select a setting:  [0] Back | [1] Give Coins | [2] Remove Coins | [3] Info/Bugs:"))
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
    elif setting == 2:
        try:
            coins_to_clear = int(input("How much Coins do you want to remove? Please enter the amount:"))
        except Exception:
            print(Fore.RED)
            print("Please enter a number")
            settings(coins)
        coins = coins - coins_to_clear
        update_coins(coins)
    elif setting == 3:
        print(
            f"{Fore.LIGHTBLUE_EX}Mini Games is a collection od classic mini and casino games with it's own money system.\n"
            f"If you want to create a bug/issue report at https://github.com/HumanBot000/MiniGames/issues please copy the text below."
            f"This makes it a lot easier to debug:"
            f"{Fore.RED}\n")
        print(f"{Fore.RED}version:{get_version()}{Fore.RESET}")
        input()
        print(Fore.RESET)
    elif setting == 0:
        main()
    print(Fore.RESET)
    settings(coins)


def validate_int(number):
    try:
        number = int(number)
    except Exception:
        return False
    else:
        if number >= 0:
            return number
        else:
            return False


def game_guess_the_number():
    clear_console()
    print(Fore.RESET)
    print(Fore.CYAN)
    try:
        game = int(input("Please select a Task:    [0] Rules | [1] Play  | [2] Back:"))
    except Exception:
        print(Fore.RED)
        print("Please enter a valid number")
        game_guess_the_number()
    if game == 1:
        coins = get_coins()
        print(Fore.YELLOW)
        try:
            bet = int(input("How much do you bet?:"))
            if coins < bet:
                print(Fore.RED)
                print(f"You only have {coins} coins")
                print(Fore.RESET)
                game_guess_the_number()
            if coins < 0:
                game_guess_the_number()
        except Exception:
            print(Fore.RED)
            print("Please enter a valid number")
            game_guess_the_number()
        try:
            print(Fore.BLUE)
            mode = int(input("Which range do you choose? [0] 0-10 (5x) | [1] 0-100(x50) | [2] 0-1000(x750):"))
            print(Fore.RESET)
        except Exception:
            print(Fore.RED)
            print("Please enter a valid number")
            game_guess_the_number()
        coins = coins - bet
        if mode == 0:
            clear_console()
            print(Fore.CYAN)
            while True:
                try:
                    print(Fore.CYAN)
                    number_user = int(input("Please enter a number between 0 and 10:"))
                    if not number_user <= 10:
                        print(Fore.RED)
                        print("Please enter a valid number")
                        print(Fore.RESET)
                    else:
                        break
                except Exception:
                    print(Fore.RED)
                    print("Please enter a valid number")
                    print(Fore.RESET)
            number_bot = random.randint(0, 10)
            if number_user == number_bot:
                print(Fore.GREEN)
                print("You Won your coins will be multiply by x5")
                print(Fore.RESET)
                coins_to_give = bet * 5
                coins = coins + coins_to_give
                update_coins(coins)
                input()
                game_guess_the_number()
            else:
                print(Fore.RED)
                print(f"You lose the bot had {number_bot} all your coins are gone")
                print(Fore.RESET)
                update_coins(coins)
                input()
                game_guess_the_number()
        elif mode == 1:
            clear_console()
            print(Fore.CYAN)
            while True:
                try:
                    print(Fore.CYAN)
                    number_user = int(input("Please enter a number between 0 and 100:"))
                    if not number_user <= 100:
                        print(Fore.RED)
                        print("Please enter a valid number")
                        print(Fore.RESET)
                    else:
                        break
                except Exception:
                    print(Fore.RED)
                    print("Please enter a valid number")
                    print(Fore.RESET)
            number_bot = random.randint(0, 100)
            if number_user == number_bot:
                print(Fore.GREEN)
                print("You Won your coins will be multiply by x50")
                print(Fore.RESET)
                coins_to_give = bet * 50
                coins = coins + coins_to_give
                update_coins(coins)
                input()
                game_guess_the_number()
            else:
                print(Fore.RED)
                print(f"You lose the bot had {number_bot} all your coins are gone")
                print(Fore.RESET)
                update_coins(coins)
                input()
                game_guess_the_number()
        elif mode == 2:
            clear_console()
            print(Fore.CYAN)
            while True:
                try:
                    print(Fore.CYAN)
                    number_user = int(input("Please enter a number between 0 and 1000:"))
                    if not number_user <= 1000:
                        print(Fore.RED)
                        print("Please enter a valid number")
                        print(Fore.RESET)
                    else:
                        break
                except Exception:
                    print(Fore.RED)
                    print("Please enter a valid number")
                    print(Fore.RESET)
            number_bot = random.randint(0, 1000)
            if number_user == number_bot:
                print(Fore.GREEN)
                print("You Won your coins will be multiply by x750")
                print(Fore.RESET)
                coins_to_give = bet * 750
                coins = coins + coins_to_give
                update_coins(coins)
                input()
                game_guess_the_number()
            else:
                print(Fore.RED)
                print(f"You lose the bot had {number_bot} all your coins are gone")
                print(Fore.RESET)
                update_coins(coins)
                input()
                game_guess_the_number()
        else:
            game_guess_the_number()
    if game == 0:
        print(Fore.GREEN)
        print(
            "Inputs: \n bet: [a number between 0 and your  coins] the bet you like to set \n range[1-3] \n guess[0-range] your guess \n"
            "First you set your coins to bet\n"
            "After that you decide for a range than higher the range is, than higher is also the multiplier\n"
            "Then you have to choose a number.Your goal is to have the same number like the bot.")
        input()
        print(Fore.RESET)
        game_black_jack()
    if game == 2:
        get_game()


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
                input()
            if bet < 0:
                print("please enter a valid number")
                input()
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
                    f"The Maximum is 20,you have{Fore.RED} {own_amount} {Fore.MAGENTA}what do you like to do? [0] Reveal Dealers Score | [1] Raise Score:"))
            except Exception:
                print(Fore.RED)
                print("Please enter a valid number")
            else:
                if option == 0:
                    dealer_amount = 19
                    while True:
                        probability = random.randint(1, 100)
                        if probability <= 70 and probability > 0:  # 70 %
                            dealer_amount = dealer_amount - 1
                        else:
                            break
                    if own_amount == dealer_amount:
                        print(Fore.YELLOW)
                        print("Its a draw you get your coins back")
                        print(Fore.RESET)
                        coins = coins + bet
                        update_coins(coins)
                        input()
                        game_black_jack()
                    elif own_amount > dealer_amount:
                        print(Fore.GREEN)
                        print(f"You won the dealer had {dealer_amount} points your coins will be multiply by 2x")
                        print(f"now you have {coins + bet + bet} coins")
                        print(Fore.RESET)
                        coins = coins + bet + bet
                        update_coins(coins)
                        input()
                        game_black_jack()
                    elif own_amount < dealer_amount:
                        print(Fore.RED)
                        print(f"You loosed the dealer had {dealer_amount} points your coins are gone")
                        print(Fore.RESET)
                        update_coins(coins)
                        input()
                        game_black_jack()
                if option == 1:
                    own_amount = own_amount + random.randint(1, 5)
                    if own_amount > 20:
                        print(Fore.RED)
                        print(f"You Lose your score is now {own_amount} your points are gone")
                        print(Fore.RESET)
                        update_coins(coins)
                        input()
                        game_black_jack()
    if game == 0:
        print(Fore.GREEN)
        print("Inputs: \n bet: [a number between 0 and your  coins] the bet you like to set \n action:[0,1]\n "
              "The Game: after you set your bet you have to decide if you raise your score or compare to dealer. \n "
              "If you raise the score it will be raised by a random number between 1 and 5.\n"
              "The goal is to reach the highest score.But be carefully if your score gets over 20 the game will end any you loes your coins.\n"
              "If you compare to the dealer the dealer starts at 19 and with a probability of 70% it will go one lower.\n"
              "Coins: You lose = bet is gone\n"
              "Draw = get your bet back\n"
              "Win = multiple by 2 ")
        input()
        print(Fore.RESET)
        game_black_jack()
    if game == 2:
        get_game()


def game_jackpot():
    clear_console()
    print(Fore.CYAN)
    coins = get_coins()
    coins_start = coins
    task = str(input("Please select a Task:    [0] Rules | [1] Play  | [2] Back:"))
    if validate_int(task) == False and task != "0":
        print(Fore.RED)
        print("Please enter a valid number")
        print(Fore.RESET)
        game_jackpot()
    else:
        if validate_int(task) >= 0 and validate_int(task) <= 2:
            task = int(task)
            if task == 0:
                print(Fore.GREEN)
                print(f"Inputs: \n bet: [a number between 0 and your  coins] the bet you like to set \n action:[0,1]\n"
                      f"The Game:you have a multiplier at the beginning its by x0 than you decide if you want to raise it \n"
                      f"or end the game if you raise it you have a 40% chance to double the multiplier 0 -> 2 -> 4 -> ...\n"
                      f"If you are unlucky all your coins are away\n"
                      f"Note if you end with a x0 multiplier your coins are also gone")
                input()
                game_jackpot()
                print(Fore.RESET)
            elif task == 1:
                print(Fore.YELLOW)
                bet = validate_int(input(f"How much do you bet?:"))
                print(Fore.RESET)
                if bet == False:
                    game_jackpot()
                else:
                    if bet <= coins:
                        coins = coins - bet
                        multiplier = 0
                        while True:
                            task = validate_int(
                                input(f"{Fore.MAGENTA}The multiplier is now {Fore.RED}x{multiplier}{Fore.MAGENTA}\n"
                                      f"What do you do?   [0] End Game | [1] Raise Multiplier:{Fore.RESET}"))
                            if task == 0:
                                coins_tg = bet * multiplier
                                coins = coins + coins_tg
                                update_coins(coins)
                                print(
                                    f"{Fore.GREEN}You ended with x{multiplier}{Fore.RESET}")
                                input()
                                game_jackpot()
                            if task == 1:
                                if random.randint(1, 10) <= 4:  # 40%
                                    if multiplier == 0:
                                        multiplier = 2
                                    else:
                                        multiplier = multiplier * 2
                                else:
                                    update_coins(coins)
                                    print(
                                        f"{Fore.RED}You lost all your coins are gone{Fore.RESET}")
                                    input()
                                    game_jackpot()
                    else:
                        print(f"{Fore.RED}You only have {coins} coins {Fore.RESET}")
                        input()
                        game_jackpot()
            elif task == 2:
                get_game()
        else:
            print(Fore.RED)
            print("Please enter a valid number")
            print(Fore.RESET)
            game_jackpot()
    print(Fore.RESET)


def game_psr():
    clear_console()
    print(Fore.CYAN)
    coins = get_coins()
    while True:
        try:
            print(Fore.CYAN)
            task = int(input("Please select a Task:    [0] Rules | [1] Play  | [2] Back:"))
        except Exception:
            print(f"{Fore.RED}Please enter a valid number{Fore.RESET}")
        else:
            break
    if task == 2:
        get_game()
    elif task == 0:
        print(Fore.GREEN)
        print("Inputs: \n bet: [a number between 0 and your  coins] the bet you like to set \n action:[1,2,3]\n"
              "The Game: \nYou don´t know the game?It´s iconic just google it.\nThe multiplier is 2x")
        print(Fore.RESET)
        input()
        game_psr()
    elif task == 1:
        while True:
            try:
                print(Fore.YELLOW)
                bet_coins = int(input("How much do you bet?:"))
            except Exception:
                print(f"{Fore.RED}Please enter a valid number{Fore.RESET}")
            else:
                if bet_coins <= int(get_coins()) and bet_coins >= 0:
                    break
                else:
                    print(f"{Fore.RED}You don´t have enough coins")
        while True:
            try:
                print(Fore.CYAN)
                p_choice = int(input("What do you choose:    [1] Paper | [2] Scissors | [3] Rock:"))
            except Exception:
                print(f"{Fore.RED}Please enter a valid number{Fore.RESET}")
            else:
                break
        b_choice = random.randint(1, 3)
        if p_choice == 1:
            if b_choice == 1:
                print(Fore.YELLOW)
                print("Its a draw you get your coins back")
                print(Fore.RESET)
                input()
                game_psr()
            elif b_choice == 2:
                print(Fore.RED)
                print(f"You loosed the bot chose {b_choice}  your coins are gone")
                print(Fore.RESET)
                coins_tg = coins - bet_coins
                update_coins(coins_tg)
                input()
                game_psr()
            elif b_choice == 3:
                print(Fore.GREEN)
                print(f"You won the bot chose {b_choice}")
                print(Fore.RESET)
                coins_tg = coins + bet_coins
                update_coins(coins_tg)
                input()
                game_psr()
        elif p_choice == 2:
            if b_choice == 2:
                print(Fore.YELLOW)
                print("Its a draw you get your coins back")
                print(Fore.RESET)
                input()
                game_psr()
            elif b_choice == 3:
                print(Fore.RED)
                print(f"You loosed the bot chose {b_choice}  your coins are gone")
                print(Fore.RESET)
                coins_tg = coins - bet_coins
                update_coins(coins_tg)
                input()
                game_psr()
            elif b_choice == 1:
                print(Fore.GREEN)
                print(f"You won the bot chose {b_choice}")
                print(Fore.RESET)
                coins_tg = coins + bet_coins
                update_coins(coins_tg)
                input()
                game_psr()
        elif p_choice == 3:
            if b_choice == 3:
                print(Fore.YELLOW)
                print("Its a draw you get your coins back")
                print(Fore.RESET)
                input()
                game_psr()
            elif b_choice == 1:
                print(Fore.RED)
                print(f"You loosed the bot chose {b_choice}  your coins are gone")
                print(Fore.RESET)
                coins_tg = coins - bet_coins
                update_coins(coins_tg)
                input()
                game_psr()
            elif b_choice == 2:
                print(Fore.GREEN)
                print(f"You won the bot chose {b_choice}")
                print(Fore.RESET)
                coins_tg = coins + bet_coins
                update_coins(coins_tg)
                input()
                game_psr()


def get_game():
    clear_console()
    print(Fore.RESET)
    print(Fore.CYAN)
    try:
        game = int(
            input(
                "Please select a game:    [0] Back | [1] Guess the Number | [2] Black Jack | [3] Jackpot Game [4] Paper-Scissors-Rock:"))
    except Exception:
        print(Fore.RED)
        print("Please enter a valid number")
        get_game()
    if game == 1:
        game_guess_the_number()
    elif game == 2:
        game_black_jack()
    elif game == 3:
        game_jackpot()
    elif game == 4:
        game_psr()
    elif game == 0:
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
        print(Fore.GREEN)
        print("""Actions: You have to enter the number in the brackets([ and ]) before the Action this is how to navigate through menus
            Economy:You have an specific balance on your bank you will see it at the main screen.If you win in games you will multiple your money.If you haven´t enough money you can cheat some in the settings
        """)
        main()
    if game == 1:
        settings(coins)
    if game == 2:
        get_game()
    else:
        main()


main()
