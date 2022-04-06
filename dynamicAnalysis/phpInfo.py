import requests
from colorama import init, Fore, Back, Style
import dynamicAnalysis.Exploit as Exploit

def PHPInfo(URL, HEADERS, COOKIES, phpInfoURL, HOST_IP, IS_AUTO_EXPLOIT):
    print()
    print()
    print(Fore.BLACK + Back.WHITE + "@ =============== PHP Info Page Exploit ===============")
    print("!")
    print("!")
    print("! Testing if :  <" + phpInfoURL + "> is vulnerable LFI with PHPInfo assistance. ")
    print("! Vulnerable LFI Path  :  " + URL)
    print("!")

    COUNT = 0
    res = requests.post(url=phpInfoURL, headers=HEADERS, cookies=COOKIES, files={"name": "testName", "filename": "testFileName"}, timeout=5)
    RESULT_TEXT = res.text
    if res.status_code == 200:
        if '[tmp_name] =&gt' in RESULT_TEXT:
            COUNT += 1
            print("! Vulnerable  :  " + phpInfoURL)
            if IS_AUTO_EXPLOIT:
                exploit = Exploit.ExploitClass(COOKIES, HOST_IP, URL, phpInfoURL)
                exploit.exploitPHPInfo()
                pass
    if COUNT == 0:
        print("!")
        print("!")
        print(Fore.GREEN + "! #################################################### !")
        print(Fore.GREEN + "! Web App " + Fore.BLACK + Back.GREEN + " is NOT vulnerable " + Fore.GREEN + Back.RESET + " to PHP Info Page attacks !")
        print(Fore.GREEN + "! #################################################### !")
    else:
        print("!")
        print("!")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")
        print(Fore.RED + "! Web App " + Fore.BLACK + Back.RED + " IS VULNERABLE " + Fore.RED + Back.RESET + " to PHP Info Page attacks !")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")
    print("!")
    print("!")
    print("! PHP Info Page Exploit !")
    print("!")
    print("!")
    return 0