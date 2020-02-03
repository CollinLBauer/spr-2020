import hashlib
import re
import os
import threading
import sys
import itertools

# helper method
# uses regular expressions to search for a submitted hash
def compareHashes(passCount, hashFile, testWord, outFile):
    #reset hash file pointer & hash word
    hashFile.seek(0)
    testHash = hashlib.sha256(testWord.encode("utf-8")).hexdigest()

    for hash in hashFile:
        hash = hash.strip("\n")
        hashList = hash.split(":")
        if(hashList[1] == testHash):
            passCount += 1
            print("{}: {} <{}>".format(hashList[0], testWord, hashList[1]))
            file = open(outFile, "a")
            file.write("{}: {}\n".format(hashList[0], testWord))
            file.close()

    return passCount

# a seven char word from /usr/share/dict/words which gets the first letter
# capitalized and a 1-digit number appended
def ruleA(passCount, inFile, hashCount, outFile, dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")

    for word in dict:
        word = word.strip("\n")
        if len(word) == 7:
            for i in range(10):
                temp = word.capitalize() + str(i)
                passCount = compareHashes(passCount, inFile, temp, outFile)
                #print(passCount)
                if passCount == hashCount:
                    dict.close()
                    return passCount

    dict.close()
    return passCount


# a five digit password with at least one of the following special
# characters in the beginning: *,~,!,#
def ruleB(passCount, inFile, hashCount, outFile):
    spec = ["*","~","!","#"]
    products = itertools.product("*~!#0123456789", repeat = 4)
    for prod in products:
        last4 = "".join(prod)
        for x in range(4):
            word = (spec[x] + last4)
            word.strip("\n")
            passCount = compareHashes(passCount, inFile, word, outFile)
            if passCount == hashCount:
                return passCount
    return passCount


# a five char word from /usr/share/dict/words with the letter 'a' in it which
# gets replaced with the special character '@' and the character 'l' which is
# substituted with the number '1'
def ruleC(passCount, inFile, hashCount, outFile, dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")

    for word in dict:
        ## Remove new line character, so that it really checks for words that are length 5
        word = word.strip("\n")
        ## This rule only cares about words of length 5 and including the letter
        ## a.  Check for these conditions.
        if(len(word) == 5 and ('a' in word or 'A' in word or 'l' in word or 'L' in word)):
            ## Create letter replacements
            word = word.replace('a', '@')
            word = word.replace('A', '@')
            word = word.replace('l','1')
            word = word.replace('L','1')
            ## This if statement only checks for uppercase passwords
            passCount = compareHashes(passCount, inFile, word, outFile)
            if passCount == hashCount:
                dict.close()
                return passCount

    dict.close()
    return passCount


# any word that is made with digits up to 7 digits length
def ruleD(passCount, inFile, hashCount, outFile):
    for x in range(10):
        ## Checks for a single digit number
        word = str(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
    for x in range(100):
        ## Checks for double digit number
        word = "{:02}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
    for x in range(1000):
        ## Checks for triple digit number
        word = "{:03}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
    for x in range(10000):
        ## Checks for quadruple digit number
        word = "{:04}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
    for x in range(100000):
        ## Checks for quintuple digit number
        word = "{:05}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
    for x in range(1000000):
        ## Checks for sextuple digit number
        word = "{:06}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
    for x in range(10000000):
        ## Checks for septuple digit number
        word = "{:07}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount

    return passCount


# any number of chars single word from /usr/share/dict/words
def ruleE(passCount, inFile, hashCount, outFile, dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")

    ## This is a simple dictionary search.
    ## Hash each word in the dictionary list and compare to given hashes.
    ## If the hash does not match, check the hashed capitalized word.
    for word in dict:
        word = word.strip("\n")
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            dict.close()
            return passCount
        ## Capitalize word if no lowercase.
        word = word.capitalize()
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            dict.close()
            return passCount

    dict.close()
    return passCount


def main():
    # check to see if arguments are valid
    outFile = "passWords.txt"
    file = open(outFile, "w")
    file.close()
    args = sys.argv
    if len(args) != 2:
        print("Expected one argument and received {}.".format(len(args)-1))
        return
    # open file and check length
    hashFile = open(args[1],"r")
    hashCount = 0
    for line in hashFile:
        hashCount += 1
    hashFile.seek(0)

    passCount = 0

    passCount = ruleB(passCount, hashFile, hashCount, outFile)

    if passCount < hashCount:
        passCount = ruleC(passCount, hashFile, hashCount, outFile)

    if passCount < hashCount:
        passCount = ruleA(passCount, hashFile, hashCount, outFile)

    if passCount < hashCount:
        passCount = ruleE(passCount, hashFile, hashCount, outFile)

    if passCount < hashCount:
        passCount = ruleD(passCount, hashFile, hashCount, outFile)

    if passCount < hashCount:
        print("{} hashes not found.".format(hashCount - passCount))

    # close file
    hashFile.close()
    print("Done.")

main()
