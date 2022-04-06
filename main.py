import os
from colorama import init, Fore, Back, Style
from dynamicAnalysis import dynamicAnalysis
from staticAnalysis import staticAnalysis

init(autoreset=True)

def main():
    os.system('cls||clear')
    print()
    print()
    print(Fore.YELLOW + "     .____   ___________.__            .___            ")
    print(Fore.YELLOW + "     |    |  \_   _____/|__| ____    __| _/___________ ")
    print(Fore.YELLOW + "     |    |   |    __)  |  |/    \  / __ |/ __ \_  __ \\")
    print(Fore.YELLOW + "     |    |___|     \   |  |   |  \/ /_/ \  ___/|  | \/")
    print(Fore.YELLOW + "     |_______ \___  /   |__|___|  /\____ |\___  >__|   ")
    print(Fore.YELLOW + "             \/   \/            \/      \/    \/       ")
    print()
    print("       Dynamic & Static LFI analysis for your web app")
    print()
    print("                  Team RememberingIan")
    print()
    print()
    print()
    print("       Please select operation,")
    print()
    print(Fore.CYAN + "       1) Dynamic App Analysis")
    print(Fore.MAGENTA + "       2) Static Code Analysis")
    print()
    print()

    while True:
        try:
            CHOICE = int(input(Fore.GREEN + "--> "))
        except ValueError:
            print(Fore.RED + "Input error, please try again")
        else:
            break

    if CHOICE == 1:
        os.system('cls||clear')
        print(Fore.BLACK + Back.WHITE + "                                   ")
        print(Fore.BLACK + Back.WHITE + "     Starting Dynamic Analysis     ")
        print(Fore.BLACK + Back.WHITE + "                                   ")
        dynamicAnalysis.main()
    else:
        os.system('cls||clear')
        print(Fore.BLACK + Back.WHITE + "                                  ")
        print(Fore.BLACK + Back.WHITE + "     Starting Static Analysis     ")
        print(Fore.BLACK + Back.WHITE + "                                  ")
        staticAnalysis.main()

if __name__ == "__main__":
    main()