import requests
from colorama import init, Fore, Back, Style
from dynamicAnalysis import Baseline
import dynamicAnalysis.Exploit as Exploit

def access_log(URL, HEADERS, COOKIES, ARG, PATH_LIST, HOST_IP, IS_AUTO_EXPLOIT):
    print()
    print()
    print(Fore.BLACK + Back.WHITE + "@ =============== Access Logs ===============")
    print("!")
    print("!")
    print("! Testing on :  <" + Fore.YELLOW + str(len(ARG)) + Fore.RESET + "> URL paths from <" + PATH_LIST + ">")
    print("! Base Path  :  " + URL)
    print("!")

    COUNT = 0
    for i in ARG:
        if 'access.log' in i:
            PATH = URL + i
            res = requests.post(url=PATH, headers=HEADERS, cookies=COOKIES, timeout=5)
            RESULT_TEXT = res.text
            BASELINE_TEXT = Baseline.capture_baseline(URL, HEADERS, COOKIES)
            if res.status_code == 200:
                if RESULT_TEXT != BASELINE_TEXT:
                    COUNT += 1
                    print("! Vulnerable  :  " + PATH)
                    # If IS_AUTO_EXPLOIT option is is True, exploit the first vulnerable path via access_log
                    if IS_AUTO_EXPLOIT:
                        exploit = Exploit.ExploitClass(COOKIES, HOST_IP, URL, PATH)
                        exploit.exploitAccessLog()
                        break
    if COUNT == 0:
        print("!")
        print("!")
        print(Fore.GREEN + "! ################################################# !")
        print(Fore.GREEN + "! Web App " + Fore.BLACK + Back.GREEN + " is NOT vulnerable " + Fore.GREEN + Back.RESET + " to Access Log attacks !")
        print(Fore.GREEN + "! ################################################# !")
    else:
        print("!")
        print("!")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")
        print(Fore.RED + "! Web App " + Fore.BLACK + Back.RED + " IS VULNERABLE " + Fore.RED + Back.RESET + " to Access Log LFI attacks !")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")
    print("!")
    print("!")
    print("! Access Logs testing complete !")
    print("!")
    print("!")
    return 0