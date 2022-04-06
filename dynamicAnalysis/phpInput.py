import requests
from colorama import init, Fore, Back, Style
from dynamicAnalysis import Baseline

def php_input(URL, HEADERS, COOKIES, PAYLOAD):
    print()
    print()
    print(Fore.BLACK + Back.WHITE + "@ =============== PHP://Input ===============")
    print("!")
    print("!")
    print("! Testing on   :  "  + URL + Fore.YELLOW + "php://input")
    print("! Base Path    :  " + URL)
    print("! Test Payload :  " + Fore.YELLOW + PAYLOAD)

    PATH = URL + "php://input"

    res = requests.post(url=PATH, headers=HEADERS, cookies=COOKIES, data=PAYLOAD, timeout=5)

    RESULT_TEXT = res.text
    BASELINE_TEXT = Baseline.capture_baseline(URL, HEADERS, COOKIES)

    if RESULT_TEXT == BASELINE_TEXT:
        print("!")
        print("!")
        print(Fore.GREEN + "! ###################################################### !")
        print(Fore.GREEN + "! Web App " + Fore.BLACK + Back.GREEN + " is NOT vulnerable " + Fore.GREEN + Back.RESET + " to PHP://Input LFI attacks !")
        print(Fore.GREEN + "! ###################################################### !")
    else:
        print("!")
        print("!")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")
        print(Fore.RED + "! Web App " + Fore.BLACK + Back.RED + " IS VULNERABLE " + Fore.RED + Back.RESET + " to PHP://Input LFI attacks !")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")

    print("!")
    print("!")
    print("! PHP://Input testing complete !")
    print("!")
    print("!")
    return 0