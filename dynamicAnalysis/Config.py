from colorama import init, Fore, Back, Style
import json


def checkValidity(CONFIG_PATH):
    FILE_CONTENT = ""
    MATCH = ["Main", "HTTP.Attributes", "Exploit.Attributes"]

    # Check if config file exists
    try:
        f = open(CONFIG_PATH, "r")
        FILE_CONTENT = f.read()
        f.close()
    except IOError:
        try:
            createClean(CONFIG_PATH)
        except IOError:
            print(Fore.RED + " !! Error Creating Config file !!")
        print()
        print()
        print(Fore.YELLOW + "Config file was missing, please modify the newly created " + Fore.BLACK + Back.YELLOW + " config.json ")
        print()
        print()
        exit()

    # Check if existing file is valid
    if not all(x in FILE_CONTENT for x in MATCH):
        print()
        print()
        print(Fore.YELLOW + "Config file contains error(s), please fix " + Fore.BLACK + Back.YELLOW + " config.json ")
        print()
        print()
        print("       Please select operation,")
        print()
        print(Fore.GREEN + "       1) Exit program and fix manually (Default)")
        print(Fore.RED + "       2) Clear config file and reset to default")
        print()
        print()
        CHOICE = input(Fore.GREEN + "--> ")
        if CHOICE == "2":
            createClean(CONFIG_PATH)
            print()
            print()
            print(Fore.GREEN + "New config file created! Please modify config file")
            print(Fore.GREEN + "Exiting cleanly")
            print()
            print()
            exit()
        else:
            print()
            print()
            print(Fore.GREEN + "No changes made, please modify config file")
            print(Fore.GREEN + "Exiting cleanly")
            print()
            print()
            exit()

def createClean(CONFIG_PATH):
    f = open(CONFIG_PATH, "w")
    data = {
        "Main": {
            "TargetURL": "",
            "PHPInfoURL": "",
            "PHPInputPayload": "<?php system('ls -l'); ?>",
            "LFIPathList": "lfi_paths.txt"
        },
        "HTTP.Attributes": {
            "Headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
                "Upgrade-Insecure-Requests": "1",
                "DNT": "1",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate"
            },
            "Cookies": {
            }
        },
        "Exploit.Attributes": {
            "NetcatAutoExploit": False,
            "NetcatHostIP": ""
        }
    }
    json.dump(data, f)