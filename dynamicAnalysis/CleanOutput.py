import re

def cleanOutput(RAW_INPUT):
    if "<!" in RAW_INPUT:
        reg = '(?s)<!?(.*?)</html>'
    elif "<HTML":
        reg = '(?s)<HTML?(.*?)</HTML>'
    else:
        reg = '(?s)<html?(.*?)</html>'

    CLEANED = re.sub(reg, '', RAW_INPUT, re.DOTALL)
    return CLEANED