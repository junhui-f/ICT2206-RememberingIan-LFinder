import os
import re
import sys
from datetime import datetime
from colorama import Fore, Back, init
init(autoreset=True)

from .indicators.indicators import *
from .util import *

source = os.path.dirname(__file__)
parent = os.path.dirname(source)
output_directory = os.path.join(source, 'output')
output_file = os.path.join(output_directory, datetime.now().strftime("%d%m%y_%H%M%S")+'-static_analysis_output.txt' )

class StaticAnalysis():
    def __init__(self):
        # Verbose
        self.verbose = False 

        self.vulns_detected = []
        self.analyzed_files = []

    def add_vulnerability(self, vuln_type, vuln_file_path, vuln_code, vuln_line_no, vuln_declaration_text, vuln_declaration_line_no):
        self.vulns_detected.append({

            "vuln_type": vuln_type,
            "vuln_file_path": vuln_file_path,
            "vuln_code": vuln_code,
            "vuln_line_no": vuln_line_no,
            "vuln_declaration_text": vuln_declaration_text,
            "vuln_declaration_line_no": vuln_declaration_line_no

        })

    def print_vulnerabilities(self):
        print(Fore.RED + "! Total Vulnerabilities Detected: %i" % (len(self.vulns_detected)))
        # Verbose
        if self.verbose:
            print("\nFiles Analyzed: ")
            for index, file in enumerate(self.analyzed_files):
                print("File %i: %s " % (index+1, file))

        for vuln in self.vulns_detected:
            print(Fore.RED + "\nPotential vulnerability found: %s" % (vuln['vuln_type']))
            print("File: %s" % (vuln['vuln_file_path']))
            print("Line %s: %s" % (vuln['vuln_line_no'], vuln['vuln_code']))
            print("Declared at Line %s: %s" % (vuln['vuln_declaration_line_no'], vuln['vuln_declaration_text']))
    
    def print_output_vanilla(self):
        print("! Total Files Analyzed: %i" % (len(self.analyzed_files)))
        if len(self.vulns_detected) > 0:
            print("! Total Vulnerabilities Detected: %i" % (len(self.vulns_detected)))
            # Verbose
            if self.verbose:
                print("\nFiles Analyzed: ")
                for index, file in enumerate(self.analyzed_files):
                    print("File %i: %s " % (index+1, file))

            for vuln in self.vulns_detected:
                print("\nPotential vulnerability found: %s" % (vuln['vuln_type']))
                print("File: %s" % (vuln['vuln_file_path']))
                print("Line %s: %s" % (vuln['vuln_line_no'], vuln['vuln_code']))
                print("Declared at Line %s: %s" % (vuln['vuln_declaration_line_no'], vuln['vuln_declaration_text']))
        else:
            print("! No Vulnerabilities Found!")   

    def print_output(self):
        print()
        print(Fore.BLACK + Back.GREEN + "                                  ")
        print(Fore.BLACK + Back.GREEN + "        Analysis Complete.        ")
        print(Fore.BLACK + Back.GREEN + "                                  ")
        print("! Total Files Analyzed: %i" % (len(self.analyzed_files)))
        if len(self.vulns_detected) > 0:
            self.print_vulnerabilities()
        else:
            print(Fore.GREEN + "! No Vulnerabilities Found!")   

    def save_to_file(self):
        original_stdout = sys.stdout
        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
        with open(output_file, 'w+') as f:
            sys.stdout = f 
            self.print_output_vanilla()
        
        sys.stdout = original_stdout
        print(Fore.GREEN + "Output has been saved to: {path}".format(path=os.path.realpath(f.name)))

    def add_analyzed_file(self, file):
        if file not in set(self.analyzed_files):
            self.analyzed_files.append(file)

    def analyze_indicators(self, file):
        if self.verbose:
            print(Fore.CYAN + "Analyzing file %s" % (file))

        code = open(file, 'r', encoding='utf-8').read()
        code = clean_code(code)

        indicators_payloads = payloads

        # payload [0] = Vulnerable Code Indicator
        # payload [1] = Indicator Name/Type
        for payload in indicators_payloads:
            regex = re.compile(payload[0] + regex_indicators)
            matches = regex.findall(code)
            # Preliminary checks
            for vuln_code in matches:
                vuln_code = list(vuln_code)

                vuln_declaration_text = ""
                vuln_declaration_line_number = ""

                line = "".join(vuln_code)
                regex = re.compile(regex_indicators[2:-2])

                for vuln_var in regex.findall(line):
                    is_vulnerable = False

                    if not is_exception(vuln_var[1]):
                        # Look for the declaration. 
                        is_vulnerable, vuln_declaration_text, vuln_declaration_line_number = find_declaration(code, vuln_var[1], file)
                    
                    if is_vulnerable:
                        line_found, vuln_code, vuln_line_no = find_line_vuln(payload, vuln_code, code)
                        if line_found:
                            self.add_vulnerability(payload[1], file, vuln_code, vuln_line_no, vuln_declaration_text, vuln_declaration_line_number)

        self.add_analyzed_file(file)
                        
    def analyzeFile(self, file):
        if os.path.exists(file):
            self.analyze_indicators(file)
        else:
            print(Fore.RED + "{file} not found!".format(file = file))
            
    def analyzeDirectory(self, path):
        if os.path.exists(path):
            php_files = [
                os.path.join(root, file_name)
                for root, dir_names, file_names in os.walk(path)
                for file_name in file_names
                if file_name.endswith(".php")
            ]

            for file in php_files:
                self.analyzeFile(file)
        
        else:
            print(Fore.RED + "{path} not found!".format(path = path))

def main():
    StaticAnalyzerInfo = StaticAnalysis()

    # For Verbose Output (e.g., show analyzed files, idk whether to keep this though.)
    StaticAnalyzerInfo.verbose = False
    output_verbosity = 0
    user_path = ""

    while True:
        try:
            print("Please select output,")
            print()
            print(Fore.CYAN + "1) Verbose")
            print(Fore.MAGENTA + "2) Non-verbose")
            print()
            output_verbosity = int(input(Fore.GREEN + "--> "))
            if output_verbosity == 1 or output_verbosity == 2:
                break
            else:
                print(Fore.RED + "Not a valid choice. Try again.")
        except ValueError:
            print(Fore.RED + "Input error, please try again")

    while True:
        try:
            print()
            print("Please input the file / directory path")
            print(Fore.GREEN + "--> ", end="")
            user_path = input()
            if os.path.exists(user_path):
                break
            else:
                print(Fore.RED + "Not a valid path. Try again.")
        except Exception as e:
            print(Fore.RED + "Input error, please try again")

    if output_verbosity == 1: StaticAnalyzerInfo.verbose = True

    # If file || Directory 
    if os.path.isdir(user_path):
        StaticAnalyzerInfo.analyzeDirectory(user_path)
    elif os.path.isfile(user_path):
        StaticAnalyzerInfo.analyzeFile(user_path)

    StaticAnalyzerInfo.print_output()
    StaticAnalyzerInfo.save_to_file()