import hashlib
import re
import os
import threading
import sys

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
    for i in spec:
        for num in range(10000): # 1 special character, 4 numbers
            word = "{}{:04}".format(i,num)
            passCount = compareHashes(passCount, inFile, word, outFile)
            if passCount == hashCount:
                    return passCount
        for j in spec:
            for num in range(1000): # 2 special characters, 3 numbers
                word = "{}{}{:03}".format(i,j,num)
                passCount = compareHashes(passCount, inFile, word, outFile)
                if passCount == hashCount:
                    return passCount
            for k in spec:
                for num in range(100): # 3 special characters, 2 numbers
                    word = "{}{}{}{:02}".format(i,j,k,num)
                    passCount = compareHashes(passCount, inFile, word, outFile)
                    if passCount == hashCount:
                        return passCount
                for l in spec:
                    for num in range(10): # 4 special characters, 1 number
                        word = "{}{}{}{}{:01}".format(i,j,k,l,num)
                        passCount = compareHashes(passCount, inFile, word, outFile)
                        if passCount == hashCount:
                            return passCount
                    for m in spec: # 5 special characters
                        word = "{}{}{}{}{}".format(i,j,k,l,m)
                        passCount = compareHashes(passCount, inFile, word, outFile)
                        if passCount == hashCount:
                            return passCount

    return passCount


# a five char word from /usr/share/dict/words witht he letter 'a' in it which
# gets replaced with the special character '@' and the character 'l' which is
# substituted with th number '1'
def ruleC(passCount, inFile, hashCount, outFile, dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")

    for word in dict:
        ## Remove new line character, so that it really checks for words that are length 5
        word = word.strip("\n")
        ## This rule only cares about words of length 5 and including the letter
        ## a.  Check for these conditions.
        if(len(word) == 5 and ('a' in word or 'A' in word)):
            word = word.lower()
            ## Create letter replacements
            word = word.replace('a', '@')
            word = word.replace('l','1')

            ## This if statement only checks for uppercase passwords
            passCount = compareHashes(passCount, inFile, word, outFile)
            if passCount == hashCount:
                dict.close()
                return passCount

            ## Need to lowercase words to check for that instance
            if(word.startswith("1") == False or word.startswith("@")== False):
                word = word.capitalize()

                ## This if statement only checks for lowercase passwords
                passCount = compareHashes(passCount, inFile, word, outFile)
                if passCount == hashCount:
                    dict.close()
                    return passCount

    dict.close()
    return passCount


# any word that is made with digits up to 7 digits length
def ruleD(passCount, inFile, hashCount, outFile):
    ## Need to use a range of 10000000 becuase the upper bound is not included
    for x in range(10000000):
        ## Format is nessecary to check for leading zeroes
        ## Checks for a single digit number
        word = "{:01}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
        ## Checks for double digit number
        word = "{:02}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
        ## Checks for triple digit number
        word = "{:03}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
        ## Checks for quadruple digit number
        word = "{:04}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
        ## Checks for quintuple digit number
        word = "{:05}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
        ## Checks for sextuple digit number
        word = "{:06}".format(x)
        passCount = compareHashes(passCount, inFile, word, outFile)
        if passCount == hashCount:
            return passCount
        ## Checks for octuple digit number
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
