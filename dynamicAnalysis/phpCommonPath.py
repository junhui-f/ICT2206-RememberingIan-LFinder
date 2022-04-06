import requests
from colorama import init, Fore, Back, Style
from dynamicAnalysis import Baseline

def php_common_path(URL, HEADERS, COOKIES, ARG, PATH_LIST):
    print()
    print()
    print(Fore.BLACK + Back.WHITE + "@ =============== PHP Common path test ===============")
    print("!")
    print("!")
    print("! Testing on :  <" + Fore.YELLOW + str(len(ARG)) + Fore.RESET + "> URL paths from <" + PATH_LIST + ">")
    print("! Base Path  :   " + URL + Fore.YELLOW + "___")
    print("!")

    COUNT = 0
    for i in ARG:
        PATH = URL + i
        res = requests.get(url=PATH, headers=HEADERS, cookies=COOKIES, timeout=5)
        RESULT_TEXT = res.text
        BASELINE_TEXT = Baseline.capture_baseline(URL, HEADERS, COOKIES)
        if res.status_code == 200:
            if RESULT_TEXT != BASELINE_TEXT:
                COUNT += 1
                print("! Vulnerable  :  " + PATH)
    if COUNT == 0:
        print("!")
        print("!")
        print(Fore.GREEN + "! ###################################################### !")
        print(Fore.GREEN + "! Web App " + Fore.BLACK + Back.GREEN + " is NOT vulnerable " + Fore.GREEN + Back.RESET + " to common path LFI attacks !")
        print(Fore.GREEN + "! ###################################################### !")
    else:
        print("!")
        print("!")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")
        print(Fore.RED + "! Web App " + Fore.BLACK + Back.RED + " IS VULNERABLE " + Fore.RED + Back.RESET + " to common path LFI attacks !")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")
    print("!")
    print("!")
    print("! PHP Common path test complete !")
    print("!")
    print("!")
    return 0