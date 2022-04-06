import os
import re

# Format the source code in order to improve the detection - see line 70 - line 78
def clean_code(code):
    # replace tab by space
    code = code.replace("    ", " ")

    return code

def is_exception(match):
    exceptions = ["_GET", "_POST", "_REQUEST", "_COOKIES", "_FILES"]
    for exception in exceptions:
        if exception in match:
            return True
    return False

def find_line_declaration(declaration, code):
    code = code.split('\n')
    for i in range(len(code)):
        if declaration in code[i]:
            return str(i+1)
    
    return "-1"

def find_line_vuln(payload, vuln, code):
    code = code.split('\n')
    for i in range(len(code)):
        try:
            if payload[0] + '(' + vuln[0] + vuln[1] + vuln[2] + ')' in code[i]:
            #if payload[0] + "".join(vuln) in code[i]:
                return True, code[i], str(i+1)
        except Exception as e:
            pass

    return False, "Line not found.", "-1"

# Cr Vulny
def find_declaration(code, vuln, file):

    regex_declaration = re.compile("(include.*?|require.*?)\\([\"\'](.*?)[\"\']\\)")
    includes = regex_declaration.findall(code)

    # Look for relative includes, and see if it is declared
    for include in includes:
        relative_include = os.path.dirname(file) + "/"
        try:
            path_include = relative_include + include[1]
            with open(path_include, 'r') as f:
                code = f.read() + code
        except Exception as e:
            return False, "Err: Declaration not found", "-1"

    vulnerability = vuln[1:]
    regex_declaration = re.compile("\\$" + vulnerability + "([\t ]*)=(?!=)(.*)")
    declaration = regex_declaration.findall(code)
    if len(declaration) > 0:

        # See if declaration of variable is a constant (which means that not vulnerable to user input LFI/RFI.)
        # $which = $_GET['which']
        declaration_text = "$" + vulnerability + declaration[0][0] + "=" + declaration[0][1]
        line_number = find_line_declaration(declaration_text, code)
        regex_constant = re.compile("\\$" + vulnerability + r"([\t ]*)=[\t ]*?([\"\'(]*?[a-zA-Z0-9{}_\\(\\)@\\.,!: ]*?[\"\')]*?);")
        match_constant = regex_constant.match(declaration_text)

        if match_constant:
            return False, "", ""
        return True, declaration_text, line_number

    return False, "Err: Declaration not found", "-1"