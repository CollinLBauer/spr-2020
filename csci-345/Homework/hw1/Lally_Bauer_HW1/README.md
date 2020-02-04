## CSCI 345 - Network Scurity

Isabel Lally, Collin Bauer

### How to run the program

1. `cd path/to/project/directory`
2. Run `python3 Lally_Bauer_HW1_passwd_cracking.py /path/to/hash/file`
2. Cracked passwords will be output to `passWords.txt` in the format `username: password`

### Testing

A test file has been provided, named `test.txt`, in the same directory.  
These test cases are in one of two formats:
- testCaseName:hash:expectedPassword
- testCaseName(expecteDPassword):hash

There are several cases for each rule in the cracking program.

Expected file output (not in order):
```
testUserA1: Puzzles4
testUserA2: Seabird7
testUserB1: ~~012
testUserB2(~!#99): ~!#99
testUserB3: #####
testUserC1: be@ch
testUserC2: Be@ch
testUserC3(hello): he11o
testUserD1: 012
testUserD2: 01234
testUserD3(0): 0
testUserD4: 9999999
testUserE1: programming
testUserE2: cats
```