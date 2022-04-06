from colorama import init, Fore, Back, Style
import json, os
import requests
from requests.structures import CaseInsensitiveDict
from dynamicAnalysis import Exploit, Config, sshAuthLog, vsftpLog
from dynamicAnalysis import phpInfo, phpInfoLFI, phpRFI, phpAccessLog, phpData, phpCommonPath, phpFilter, phpInput


def main():
    #
    # Change pwd to current file's
    #
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    #
    # Check and Load config from external file
    #
    CONFIG_PATH = os.path.join("config.json")
    Config.checkValidity(CONFIG_PATH)
    with open(CONFIG_PATH) as f:
        config = json.load(f)
    f.close()

    #
    # Load config params
    #
    IS_AUTO_EXPLOIT = config["Exploit.Attributes"]["NetcatAutoExploit"]  # If True, exploit and spawn interactive shell on the first vulnerable path found
    HOST_IP =  config["Exploit.Attributes"]["NetcatHostIP"]  # Set to ip for rev shell to connect to
    TARGET_URL = config["Main"]["TargetURL"]
    phpInfoURL = config["Main"]["PHPInfoURL"]
    PHP_INPUT_PAYLOAD = config["Main"]["PHPInputPayload"]
    HEADERS = config["HTTP.Attributes"]["Headers"]
    COOKIES = config["HTTP.Attributes"]["Cookies"]
    source = os.path.dirname(__file__)
    PATH_LIST = os.path.join(source, config["Main"]["LFIPathList"])
    with open(PATH_LIST) as f:  # Load paths into python
        ARG = [i.strip() for i in f]

    #
    # Print pending tests
    #
    print()
    print()
    print("|   Tests to be run:")
    print("|")
    print("|   1) Common LFI paths")
    print("|   2) PHP://Filter")
    print("|   3) PHP://Input")
    print("|   4) DATA://")
    print("|   5) RFI")
    print("|   6) PHP Info Page")
    print("|   7) Access Logs")
    print("|   8) SSH Auth Log")
    print("|   9) VSFTP Log")
    print("|")
    print("| - - - - - - - - - - - - - - -")
    print("|")
    print("|   Configuration options loaded from < " + Fore.YELLOW + "config.json" + Fore.RESET + " > :")
    print("|   ---")
    print("|")
    print("|   Target URL :              [ " + Fore.YELLOW + TARGET_URL + Fore.RESET + " ]")
    print("|   Target PHPInfo URL :      [ " + Fore.YELLOW + phpInfoURL + Fore.RESET + " ]")
    print("|   PHP://Input Payload :     [ " + Fore.YELLOW + PHP_INPUT_PAYLOAD + Fore.RESET + " ]")
    print("|")
    print("|   LFI Path List :           [ " + Fore.YELLOW + config["Main"]["LFIPathList"] + Fore.RESET + " ]")
    print("|")
    if HEADERS:
        print("|   Headers Loaded :          [ " + Fore.GREEN + "True" + Fore.RESET + " ]")
    else:
        print("|   Headers Loaded :          [ " + Fore.RED + "False" + Fore.RESET + " ]")
    if COOKIES:
        print("|   Cookies Loaded :          [ " + Fore.GREEN + "True" + Fore.RESET + " ]")
    else:
        print("|   Cookies Loaded :          [ " + Fore.RED + "False" + Fore.RESET + " ]")
    print("|")
    if IS_AUTO_EXPLOIT:
        print("|   Auto Exploit :            [ " + Fore.GREEN + "True" + Fore.RESET + " ]")
        print("|   Netcat Host IP :          [ " + Fore.GREEN + HOST_IP + Fore.RESET + " ]")
    else:
        print("|   Auto Exploit :            [ " + Fore.RED + "False" + Fore.RESET + " ]")

    #
    # Perform actions
    #
    print()
    print()
    print()
    print(Fore.MAGENTA + "       Begin tests ? ")
    print("       ---")
    print()
    print("       < "  + Fore.GREEN + "Y" + Fore.RESET + " > or  < " + Fore.GREEN + "y" + Fore.RESET + " > to start")
    print("                  or")
    print("       Another other key to quit")
    print()
    CHOICE = input(Fore.GREEN + "--> ")
    print()
    print()

    if CHOICE == "y" or CHOICE == "Y":
        try:
            OUTPUT_1 = phpCommonPath.php_common_path(TARGET_URL, HEADERS, COOKIES, ARG, PATH_LIST)
            OUTPUT_2 = phpFilter.php_filter(TARGET_URL, HEADERS, COOKIES, ARG, PATH_LIST)
            OUTPUT_3 = phpInput.php_input(TARGET_URL, HEADERS, COOKIES, PHP_INPUT_PAYLOAD)
            OUTPUT_4 = phpData.php_data(TARGET_URL, HEADERS, COOKIES, ARG, PATH_LIST, HOST_IP, IS_AUTO_EXPLOIT)
            OUTPUT_5 = phpRFI.RFI(TARGET_URL, HEADERS, COOKIES, ARG, PATH_LIST, HOST_IP, IS_AUTO_EXPLOIT)
            OUTPUT_6 = phpInfo.PHPInfo(TARGET_URL, HEADERS, COOKIES, phpInfoURL, HOST_IP, IS_AUTO_EXPLOIT)
            OUTPUT_7 = phpAccessLog.access_log(TARGET_URL, HEADERS, COOKIES, ARG, PATH_LIST, HOST_IP, IS_AUTO_EXPLOIT)
            OUTPUT_8 = sshAuthLog.SSH_auth_log(TARGET_URL, HEADERS, COOKIES, ARG, PATH_LIST, HOST_IP, IS_AUTO_EXPLOIT)
            OUTPUT_9 = vsftpLog.vsftp_log(TARGET_URL, HEADERS, COOKIES, ARG, PATH_LIST, HOST_IP, IS_AUTO_EXPLOIT)
        except requests.exceptions.MissingSchema:
            os.system('cls||clear')
            print()
            print()
            print(Fore.RED + " !! Error in config file !!")
            print()
            print()
            exit()
        except requests.exceptions.RequestException as e:
            print("!")
            print("!")
            print("! " + Fore.RED + " Connection timed out, ensure provided URL is correct ")
            print("!")
            print("!")
            print("!")
            print("! =========================================")


if __name__ == "__main__":
    main()