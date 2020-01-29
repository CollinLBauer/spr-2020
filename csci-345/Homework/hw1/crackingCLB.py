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

# a five digit password with at least one of the following special
# characters in the beginning: *,~,!,#
def ruleB(inFile):
    for i in ["*","~","!","#"]:
        for j in range(100000):
            word = "{}{:05}".format(i,j)
            hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
            if compareHashes(inFile,hash):
                return word, hash

    return -1, -1

# a five char word from /usr/share/dict/words witht he letter 'a' in it which
# gets replaced with the special character '@' and the character 'l' which is
# substituted with th number '1'
def ruleC(inFile,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    #TODO
    dict.close()
    pass

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
    args = sys.argv
    if len(args) <= 1:
        print("Argument expected.")
        return

    hashFile = open(args[1],"r")

    word, hash = ruleB(hashFile)
    print("Word: " + word)
    print("Hash: " + hash)

    hashFile.close()

main()
