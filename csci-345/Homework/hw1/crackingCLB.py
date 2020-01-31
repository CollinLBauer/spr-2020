import hashlib
import re
import os
import threading
import sys

# helper method
# uses regular expressions to search for a submitted hash
def compareHashes(passCount, hashFile, testWord):
    #reset hash file pointer & hash word
    hashFile.seek(0)
    testHash = hashlib.sha256(testWord.encode("utf-8")).hexdigest()

    for hash in hashFile:
        hash = hash.strip("\n")
        hashList = hash.split(":")
        if(hashList[1] == testHash):
            passCount += 1
            print("{}: {} <{}>".format(hashList[0], testWord, hashList[1]))

    return passCount

# a seven char word from /usr/share/dict/words which gets the first letter
# capitalized and a 1-digit number appended
def ruleA(passCount, inFile, hashCount, dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    
    for word in dict:
        word = word.strip("\n")
        if len(word) == 7:
            for i in range(10):
                temp = word.capitalize() + str(i)
                passCount = compareHashes(passCount, inFile, temp)
                #print(passCount)
                if passCount == hashCount:
                    print("Exiting early.")
                    dict.close()
                    return passCount

    dict.close()
    return passCount

'''
# a five digit password with at least one of the following special
# characters in the beginning: *,~,!,#
def ruleB(passCount, inFile):
    spec = ["*","~","!","#"]
    for i in spec:
        for num in range(10000): # 1 special character, 4 numbers
            word = "{}{:04}".format(i,num)
            hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
            if compareHashes(inFile,hash):
                return word, hash
        for j in spec:
            for num in range(1000): # 2 special characters, 3 numbers
                word = "{}{}{:03}".format(i,j,num)
                hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
                if compareHashes(inFile,hash):
                    return word, hash
            for k in spec:
                for num in range(100): # 3 special characters, 2 numbers
                    word = "{}{}{}{:02}".format(i,j,k,num)
                    hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
                    if compareHashes(inFile,hash):
                        return word, hash
                for l in spec:
                    for num in range(10): # 4 special characters, 1 number
                        word = "{}{}{}{}{:01}".format(i,j,k,l,num)
                        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
                        if compareHashes(inFile,hash):
                            return word, hash
                    for m in spec: # 5 special characters
                        word = "{}{}{}{}{}".format(i,j,k,l,m)
                        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
                        if compareHashes(inFile,hash):
                            return word, hash

    return "-1", "-1"

# a five char word from /usr/share/dict/words witht he letter 'a' in it which
# gets replaced with the special character '@' and the character 'l' which is
# substituted with th number '1'
def ruleC(passCount, inFile,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")

    for word in dict:
        ## Remove new line character, so that it really checks for words that are length 5
        word = word.strip("\n")
        ## This rule only cares about words of length 5 and including the letter
        ## a.  Check for these conditions.
        if(len(word) == 5 and ('a' in word or 'A' in word)):
            ## Create letter replacements
            word = word.replace('a', '@')
            word = word.replace('A','@')
            word = word.replace('l','1')
            word = word.replace('L','1')
            hash = hashlib.sha256(word.encode("utf-8")).hexdigest()

            ## This if statement only checks for uppercase passwords
            if(compareHashes(inFile, hash)):
                dict.close()
                return word, hash

            ## Need to lowercase words to check for that instance
            word = word.capitalize()
            hash = hashlib.sha256(word.encode("utf-8")).hexdigest()

            ## This if statement only checks for lowercase passwords
            if(compareHashes(inFile, hash)):
                dict.close()
                return word, hash

    ## If no matches are found, return values of -1, for main to manage
    dict.close()
    return "-1", "-1"


# any word that is made with digits up to 7 digits length
def ruleD(passCount, inFile):
    ## Need to use a range of 10000000 becuase the upper bound is not included
    for x in range(10000000):
        ## Format is nessecary to check for leading zeroes
        ## Checks for a single digit number
        word = "{:01}".format(x)
        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
        if(compareHashes(inFile, hash)):
            return word, hash
        ## Checks for double digit number
        word = "{:02}".format(x)
        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
        if(compareHashes(inFile, hash)):
            return word, hash
        ## Checks for triple digit number
        word = "{:03}".format(x)
        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
        if(compareHashes(inFile, hash)):
            return word, hash
        ## Checks for quadruple digit number
        word = "{:04}".format(x)
        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
        if(compareHashes(inFile, hash)):
            return word, hash
        ## Checks for quintuple digit number
        word = "{:05}".format(x)
        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
        if(compareHashes(inFile, hash)):
            return word, hash
        ## Checks for sextuple digit number
        word = "{:06}".format(x)
        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
        if(compareHashes(inFile, hash)):
            return word, hash
        ## Checks for octuple digit number
        word = "{:07}".format(x)
        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
        if(compareHashes(inFile, hash)):
            return word, hash
    ## If no password to hash is found return -1, -1
    return "-1", "-1"


# any number of chars single word from /usr/share/dict/words
def ruleE(passCount, inFile,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")

    ## This is a simple dictionary search.
    ## Hash each word in the dictionary list and compare to given hashes.
    ## If the hash does not match, check the hashed capitalized word.
    for word in dict:
        word = word.strip("\n")
        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
        if(compareHashes(inFile, hash)):
            dict.close()
            return word, hash
        ## Capitalize word if no lowercase.
        word = word.capitalize()
        hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
        if(compareHashes(inFile, hash)):
            dict.close()
            return word, hash

    ## If the hash is not found, then return -1, -1
    dict.close()
    return "-1", "-1"
'''

def main():
    # check to see if arguments are valid
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

    passCount = ruleA(passCount, hashFile, hashCount)
    '''
    if passCount < hashCount:
        ruleB()
    if passCount < hashCount:
        ruleC()
    if passCount < hashCount:
        ruleD()
    if passCount < hashCount:
        ruleE()
    '''
    if passCount < hashCount:
        print("{} hashes not found.".format(hashCount - passCount))


    # close file
    hashFile.close()
    print("Done.")

main()
