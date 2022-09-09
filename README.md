# PyWAVA Documentation

>
## Installation

The source of the software is hosted on github and should be cloned as follows:
```ps
C:\> git clone https://github.com/G4vr0ch3/PyWAVA
```
Before using the software, requirements have to be installed using:

```ps
C:\> cd PyWAVA
C:\Pywava> pip install -r requirements.txt
```

The software is now ready to be used.

## Usage

PyWAVA can be used directly from the command line or as a python library.
The “—test” flag will test the different functions of the software.

```cmd
~$ python pywava.py --test
```

The “-f” flag with an input-file path will attempt a data sanitization process on the document.

```cmd
~$ python pywava.py -f <INPUT_FILE>
```

The “-r” flag will remove the input file after treatment. The “—help” flag or “-h” flag will display the help page of the software.

Pywava can also be used as a python library using the “analyze” function to analyze the file.

```python
import pywava

pywava.analyze("input_file_path")
```

The “test” function will test the different functions of the software.

## Software overview

When the Brain retrieves the list of file to be analyzed, it feeds the information to the Analysis center that will proceed to copying the files that are to be analyzed from Frontend. The analysis Center will then scan files one by one.

| ![](pic/pywava.py) |
| :-: |
| Software architecture |

**Pywava.py**: This is the main program, it receives a file path as an argument and uses the proper library to analyze the file. It returns a document with the analysis results. It's main analyzing function will return the list of results from the different AV Solutions as well as a status.  
This status can be :
- 0: No AV Solution flagged the file as malicious.
- 1: At least one of the AV Solutions produced an unexpected result.
- 2: At least one of the AV Solutions flagged the file as malicious.

**Defender.py**: This is a library that is a wrapper for the Windows Defender Command Line Interface (CLI) software. It will return True if the file is considered innocuous, False if it is not and None if anything unexpected happened.

**Kaspersky.py**: This is a library that is a wrapper for the Kaspersky Anti Virus CLI software. It will return True if the file is considered innocuous, False if it is not and None if anything unexpected happened.

**Clamav.py**: This is a library that is a wrapper for the ClamAV CLI software. It will return True if the file is considered innocuous, False if it is not and None if anything unexpected happened.

**Hash.py**: This is a library that aims at helping in checking data integrity. It relies on the “hashlib” python library and the “sha512” (Secure Hash Algorithm-512) cryptographic hash algorithm. The main function takes a file path as an argument and returns the sha512-hash for the file.  

“hash.py” is not licensed.

**Prints.py**: This is a library that aims at printing information regarding the program’s execution using the following color code:

Green: success
Blue: information
Orange: warnings
Red: failures  

“prints.py” is not licensed.
