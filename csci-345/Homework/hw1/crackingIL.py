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
        hash = hash.strip("\n")
        hashList = hash.split(":")
        if(hashList[1] == testHash):
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
    dict.seek(0);

    for word in dict:
        word = word.strip("\n")
        if(len(word) == 5 and ('a' in word or 'A' in word)):
            word = word.replace('a', '@')
            word = word.replace('A','@')
            word = word.replace('l','1')
            word = word.replace('L','1')
            hash = hashlib.sha256(word.encode("utf-8")).hexdigest()

            if(compareHashes(inFile, hash)):
                return word, hash
            word = word.lower()
            hash = hashlib.sha256(word.encode("utf-8")).hexdigest()

            if(compareHashes(inFile, hash)):
                return word, hash

    return "-1", "-1"
    dict.close()


# any word that is made with digits up to 7 digits length
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
    if len(sys.argv) != 2:
        print("Argument expected.")
        return

    hashFile = open(sys.argv[1],"r")
    password, hash = ruleC(hashFile)
    print("password: " + password + "\nhash: " + hash)





main()
