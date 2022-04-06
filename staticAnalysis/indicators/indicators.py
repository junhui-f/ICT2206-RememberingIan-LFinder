"""
Vunerability Indicators
Taken from
https://github.com/swisskyrepo/Vulny-Code-Static-Analysis/blob/master/indicators.py
"""

# /!\ Detection Format (.*)function($vuln)(.*) matched by payload[0]+regex_indicators
regex_indicators = '\\((.*?)(\\$_GET\\[.*?\\]|\\$_FILES\\[.*?\\]|\\$_POST\\[.*?\\]|\\$_REQUEST\\[.*?\\]|\\$_COOKIES\\[.*?\\]|\\$_SESSION\\[.*?\\]|\\$(?!this|e-)[a-zA-Z0-9_]*)(.*?)\\)'

# Variable Regex
var_regex = "\$[\w\s]+\s?=\s?[\"|'].*[\"|']|define\([\"|'].*[\"|']\)"

# Function_Name:String, Vulnerability_Name:String
payloads = [

    # File Inclusion / Path Traversal
    ["virtual", "File Inclusion"],
    ["include", "File Inclusion"],
    ["require", "File Inclusion"],
    ["include_once", "File Inclusion"],
    ["require_once", "File Inclusion"],

    ["readfile", "File Inclusion / Path Traversal"],
    ["file_get_contents", "File Inclusion / Path Traversal"],
    ["file_put_contents", "File Inclusion / Path Traversal"],
    ["show_source", "File Inclusion / Path Traversal"],
    ["fopen", "File Inclusion / Path Traversal"],
    ["file", "File Inclusion / Path Traversal"],
    ["fpassthru", "File Inclusion / Path Traversal"],
    ["gzopen", "File Inclusion / Path Traversal"],
    ["gzfile", "File Inclusion / Path Traversal"],
    ["gzpassthru", "File Inclusion / Path Traversal"],
    ["readgzfile", "File Inclusion / Path Traversal"],
    
    ["DirectoryIterator", "File Inclusion / Path Traversal"],
    ["stream_get_contents", "File Inclusion / Path Traversal"],
    ["copy", "File Inclusion / Path Traversal"],
    
]