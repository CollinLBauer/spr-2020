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
testUserA_Homer: Puzzles4
testUserA1: Seabird7
testUserA2: Presley9
testUserB_Marge: ~0123
testUserB1: ~~012
testUserB2(~!#99): ~!#99
testUserB3: #####
testUserC_Lisa: be@ch
testUserC1: Be@ch
testUserC2(hello): he11o
testUserC3: 1@rge
testUserD1: 012
testUserD2: 01234
testUserD3(0): 0
testUserD4: 9999999
testUserE_Maggie: programming
testUserE1: cats
testUserE2: a
```

testUserNo: NotGonnaWork will not print to the file, since the password doesn't
follow any of the five rules.  This will test the worst case for all rules.  The
number of hashes not found will print to the console.
