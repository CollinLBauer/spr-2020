import hashlib
import re
import os
import threading
import sys

# helper method
# uses regular expressions to search for a submitted hash
def compareHashes(hashFile, testHash):
    hashFile.seek(0)

    for hash in hashFile:
        hashList = hash.split(":")
        if(hashList[1] == testHash)
            return True
    return False



# a seven char word from /usr/share/dict/words which gets the first letter
# capitalized and a 1-digit number appended
def ruleA(inFile,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    #TODO
    dict.close()
    pass

# a ten digit password with at least one of the following special
# characters in the beginning: *,~,!,#
def ruleB(inFile):
    #TODO
    pass

# a five char word from /usr/share/dict/words witht he letter 'a' in it which
# gets replaced with the special character '@' and the character 'l' which is
# substituted with th number '1'
def ruleC(inFile,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    #TODO
    dict.close()
    pass

# any word that is made with digits up to 100 digits length
def ruleD(inFile):
    #TODO
    pass

# any number of chars single word from /usr/share/dict/words
def ruleE(inFile,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    #TODO
    dict.close()
    pass


def main():
    if len(argv) <= 1:
        print("Argument expected.")
        return

    hashFile = open(argv[1],"r")
    result = ruleA(hashFile)





main()
