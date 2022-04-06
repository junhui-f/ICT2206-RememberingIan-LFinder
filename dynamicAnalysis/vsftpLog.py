import requests ,socket, re
from colorama import init, Fore, Back, Style
from dynamicAnalysis import Baseline
import dynamicAnalysis.Exploit as Exploit

def vsftp_log(URL, HEADERS, COOKIES, ARG, PATH_LIST, HOST_IP, IS_AUTO_EXPLOIT):
    print()
    print()
    print(Fore.BLACK + Back.WHITE + "@ =============== vsftp logs ===============")
    print("!")
    print("!")
    print("! Testing on :  <" + Fore.YELLOW + str(len(ARG)) + Fore.RESET + "> URL paths from <" + PATH_LIST + ">")
    print("! Base Path  :  " + URL)
    print("!")

    COUNT = 0
    for i in ARG:
        if 'vsftpd.log' in i:
            PATH = URL + i
            res = requests.get(url=PATH, headers=HEADERS, cookies=COOKIES, timeout=5)
            RESULT_TEXT = res.text
            BASELINE_TEXT = Baseline.capture_baseline(URL, HEADERS, COOKIES)

            # Check whether auth.log is accessible
            if res.status_code == 200:
                if RESULT_TEXT != BASELINE_TEXT:
                    COUNT += 1
                    print("! Vulnerable  :  " + PATH)
                    # Check whether vsftpd is running on the target
                    ip = getIP(URL)
                    port = 21
                    if checkIfPortOpen(ip, port):
                        print('! vsftp log is accessible and vsftpd is running! Might be vulnerable.')
                        # If IS_AUTO_EXPLOIT option is is True, exploit the first vulnerable path via vsftp_log
                        if IS_AUTO_EXPLOIT:
                            exploit = Exploit.ExploitClass(COOKIES, HOST_IP, URL, PATH)
                            exploit.exploitVsftpdLog(ip)
                            break
    if COUNT == 0:
        print("!")
        print("!")
        print(Fore.GREEN + "! ################################################ !")
        print(Fore.GREEN + "! Web App " + Fore.BLACK + Back.GREEN + " is NOT vulnerable " + Fore.GREEN + Back.RESET + " to VSFTP Log attacks !")
        print(Fore.GREEN + "! ################################################ !")
    else:
        print("!")
        print("!")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")
        print(Fore.RED + "! Web App " + Fore.BLACK + Back.RED + " IS VULNERABLE " + Fore.RED + Back.RESET + " to VSFTP Log LFI attacks !")
        print(Fore.RED + "! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !")
    print("!")
    print("!")
    print("! vsftp logs testing complete !")
    print("!")
    print("!")
    return 0

def getIP(url):
    try:
        ip = socket.gethostbyname(url)
    except:
        print('IP resolve failed. Attempting to extract IP with regex...')
        ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url)[0]
    return ip

def checkIfPortOpen(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    r = False
    if result == 0:
        r = True
    sock.close()
    return r