import hashlib
import re
import os
import threading
import sys

global seekLoc

# helper method
# uses regular expressions to search for a submitted hash
def compareHashes(hashFile, testHash):
    global seekLoc
    hashFile.seek(seekLoc)
    seekLoc+=1
    for hash in hashFile:
        hashList = hash.split(":")
        if(hashList[1] == testHash):
            return True
    return False



# a seven char word from /usr/share/dict/words which gets the first letter
# capitalized and a 1-digit number appended
def ruleA(inFile,seekLoc,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    word = 0

    for word in dict:
        word = word.strip("\n")
        if(len(word) == 7):
            word = word.capitalize()
            for i in range(10):
                temp = word + str(i)
                hash = hashlib.sha256(temp.encode("utf-8")).hexdigest()
                if compareHashes(inFile,hash):
                    dict.close()
                    return temp, hash

    dict.close()
    return "-1", "-1"

# a five digit password with at least one of the following special
# characters in the beginning: *,~,!,#
def ruleB(inFile):
    spec = ["*","~","!","#"]
    for i in spec:
        for num in range(10000): # 1 special character, 4 numbers
            word = "{}{:04}".format(i,num)
            hash = hashlib.sha256(word.encode("utf-8")).hexdigest()
            if compareHashes(inFile, hash):
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
def ruleC(inFile,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    #TODO
    dict.seek(0);

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
def ruleD(inFile):
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
def ruleE(inFile, dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")

    dict.seek(0);

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

    dict.close()



def main():
    global seekLoc
    args = sys.argv
    if len(args) != 2:
        print("One argument expected.")
        return

    solved = []
    word = ""
    hashFile = open(args[1],"r")
    count = len(hashFile.readlines())
    print(count)
    while(len(solved) < (2*count)):
        seekLoc = 0
        while(word != "-1"):
            word, hash = ruleB(hashFile)
            if(word != "-1"):
                solved.append(hash)
                solved.append(word)
        print(len(solved))
        seekLoc = 0
        word = ""
        print("B")
        while(word != "-1"):
            word, hash = ruleC(hashFile)
            solved.append(hash)
            solved.append(word)
        print(len(solved))
        word = ""
        seekLoc = 0
        while(word != "-1"):
            word, hash = ruleA(hashFile)
            solved.append(hash)
            solved.append(word)
        print(len(solved))
        word = ""
        seekLoc = 0
        while(word != "-1"):
            word, hash = ruleE(hashFile)
            solved.append(hash)
            solved.append(word)
        print(len(solved))
        word = ""
        seekLoc = 0
        while(word != "-1"):
            word, hash = ruleD(hashFile)
            solved.append(hash)
            solved.append(word)
        print(len(solved))
    for i in range (len(solved)):
        print(solved[i])

    hashFile.close()



main()
