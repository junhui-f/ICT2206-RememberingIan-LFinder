<p align="center"><img src="https://user-images.githubusercontent.com/1593214/161822238-4d21eabf-ded4-47ff-9aae-22f2a5a57293.png"></img></p>

<h1 align="center">LFinder - Team RememberingIan</h1>

### Members
- `2001174` Kevin Pook Yuan Kai
- `2001209` Lim Jin Tao Benjamin
- `2001267` Foong Jun Hui
- `2001558` Jeremy Jevon Chow Zi You

### Description
LFinder is a vulnerability assessment tool that provides both **dynamic analysis** and **static code analysis**.

### Objective
To provide developers with an immediate identification of any potential security weaknessess in a web application. By doing so, developers are given more time to address the situation by finding a temporary solution or to eliminate the problem entirely.

#### Key files/directories to note
```
.
├── dynamicAnalysis/
│       │
│       └── dynamicAnalysis.py ----- # Trigger point for dynamic analysis
│
│
├── staticAnalysis/
│       │
│       └── staticAnalysis.py ------ # Trigger point for static code analysis
│
│
└── main.py ------------------------ # Main launch point
```

## Dynamic Analysis
In the dynamic analysis module of LFinder, URL parameter fuzzing and various exploitation techniques are used to identify and exploit potential LFI vulnerabilities. The user is only required to pass in the URL and the cookie if needed, to start the process.

## Static Analysis
In the static analysis module of LFinder, regex, string matching and indicators are used to identify potential LFI/RFI vulnerabilities in static code files. Upon selecting the static analysis module, users are required to input the path of the desired file / directory to be analysed. After analysis,  output is printed to the terminal and saved to a text file.

## Required Libraries
- requests
- colorama

## Assumptions
The project was developed and tested on
- `Windows 10/11`
- `macOS 12`
- `DVWA` - [Damn Vulnerable Web Application](https://github.com/digininja/DVWA)

## Installation
```
git clone https://github.com/junhui-f/ICT2206-RememberingIan-LFinder
cd LFinder
pip install -r requirements.txt
```

## Documentation
### User Manual

#### Dynamic Analysis

1. Navigate to `dynamicAnalysis/`
2. Modify `config.json` to fit environment needs
```
Main - URLs and PathList
Cookies - Test environment of DVWA requires special cookie variables
Exploit.Attributes - Local netcat details
```

3. Run command to start
```
python3 main.py
```
4. Input option 1 (for dynamic analysis)

#### Static Analysis

1. Input option 2 (for static analysis)
2. Input desired output [verbosity](#verbosity)
3. Input path of file / directory to be analysed.

#### Verbosity
Verbose

> Outputs path of currently analysed file, and file paths of all analysed files post-analysis

Non Verbose

> Default setting.

**Sample output**

![image](https://user-images.githubusercontent.com/72612659/161806725-9ea28c98-22e4-4630-821f-4db448e33377.png)

Output is also saved to ~/staticAnalysis/[ddmmyy-HMS]-static_analysis_output.txt

Test files are located in [~/staticAnalysis/test_file](https://github.com/junhui-f/ICT2206-RememberingIan-LFinder/tree/main/staticAnalysis/test_file) and [~/staticAnalysis/test_directory](https://github.com/junhui-f/ICT2206-RememberingIan-LFinder/tree/main/staticAnalysis/test_directory)

### Architecture
![System Architecture](https://user-images.githubusercontent.com/1593214/161822700-19d86ed0-ddcd-41d3-aa91-4133dfb0f72f.png)

### YouTube Demonstration
[![Video](https://user-images.githubusercontent.com/27985157/161920333-e9fd959b-d2c9-4964-972b-c28d54655cb3.png)](https://youtu.be/woE_JIYXZYE)

### Poster
![Poster](https://user-images.githubusercontent.com/27985157/161921278-04d4dede-4cba-464e-8f2f-8ad3014988fc.png)
