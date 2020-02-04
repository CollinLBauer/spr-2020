import hashlib
import sys
import multiprocessing as mp

# helper method
# uses regular expressions to search for a submitted hash
def compareHashes(passCount, hashFile, testWord, outFile):
    #reset hash file pointer & hash word
    hashFile.seek(0)
    testHash = hashlib.sha256(testWord.encode("utf-8")).hexdigest()

    # compare each hash in file against test hash
    for hash in hashFile:
        hash = hash.strip("\n")
        hashList = hash.split(":")
        if(hashList[1] == testHash):  # increment counter, print results and write to output
            passCount += 1
            print("{}: {} <{}>".format(hashList[0], testWord, hashList[1]))
            outFile.append("{}: {}\n".format(hashList[0], testWord))

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
        if(len(word) == 5 and ('a' in word or 'l' in word)):
            ## Create letter replacements
            word = word.replace('a', '@')
            word = word.replace('l','1')
            ## This if statement only checks for uppercase passwords
            passCount = compareHashes(passCount, inFile, word, outFile)
            if passCount == hashCount:
                dict.close()
                return passCount

    dict.close()
    return passCount

def ruleD_01(passCount, inFile, hashCount, outFile, queue, lock):
    print("01")
    for x in range(10):
        ## Checks for a single digit number
        word = str(x)
        lock.acquire()
        passCount = compareHashes(passCount, inFile, word, outFile)
        lock.release()
    for x in range(100):
        ## Checks for double digit number
        word = "{:02}".format(x)
        lock.acquire()
        passCount = compareHashes(passCount, inFile, word, outFile)
        lock.release()
    for x in range(1000):
        ## Checks for triple digit number
        word = "{:03}".format(x)
        lock.acquire()
        passCount = compareHashes(passCount, inFile, word, outFile)
        lock.release()
    for x in range(10000):
        ## Checks for quadruple digit number
        word = "{:04}".format(x)
        lock.acquire()
        passCount = compareHashes(passCount, inFile, word, outFile)
        lock.release()
    for x in range(100000):
        ## Checks for quintuple digit number
        word = "{:05}".format(x)
        lock.acquire()
        passCount = compareHashes(passCount, inFile, word, outFile)
        lock.release()

    queue.put(passCount)

def ruleD_02(passCount, inFile, hashCount, outFile, queue, lock):
    print("02")
    for x in range(1000000):
        ## Checks for sextuple digit number
        word = "{:06}".format(x)
        lock.acquire()
        passCount = compareHashes(passCount, inFile, word, outFile)
        lock.release()

    queue.put(passCount)

def ruleD_03(passCount, inFile, hashCount, outFile, queue, lock, start):
    print("03: {}".format(start))
    for x in range(start, start + 1000000):
        ## Checks for septuple number within range of 1000000
        word = "{:07}".format(x)
        lock.acquire()
        passCount = compareHashes(passCount, inFile, word, outFile)
        lock.release()

    queue.put(passCount)

# any word that is made with digits up to 7 digits length
# This method is a helper which creates several subprocesses to do the heavy lifting
def ruleD(passCount, inFile, hashCount, outFile):
    procList = []           # process list
    output = mp.Queue()     # output queue
    lock = mp.Lock()
    
    procList.append(mp.Process(target=ruleD_01, args=(0, inFile, hashCount, outFile, output, lock)))
    procList.append(mp.Process(target=ruleD_02, args=(0, inFile, hashCount, outFile, output, lock)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 0)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 1000000)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 3000000)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 4000000)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 2000000)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 5000000)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 6000000)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 7000000)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 8000000)))
    procList.append(mp.Process(target=ruleD_03, args=(0, inFile, hashCount, outFile, output, lock, 9000000)))

    for p in procList:
        p.start()
    
    for p in procList:
        p.join()

    for p in procList:
        print("output get")
        passCount += output.get()
    
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
    args = sys.argv
    if len(args) != 2:
        print("Expected one argument and received {}.".format(len(args)-1))
        return
    
    # open output file
    # WARNING: This will overwrite anything already in the file.
    OUTPUT_NAME = "passWords.txt"
    outFile = open(OUTPUT_NAME, "w")
    outList = []

    # open hash file and check length
    hashFile = open(args[1],"r")
    hashCount = 0
    for line in hashFile:
        hashCount += 1
    hashFile.seek(0)

    # number of found passwords
    passCount = 0

    # run the hashes through each of the rules
    # If the pass count is ever equal to the length, it will exit early.
    # These should be organized by their time efficiency.
    passCount = ruleD(passCount, hashFile, hashCount, outList)
    
    if passCount < hashCount:
        passCount = ruleC(passCount, hashFile, hashCount, outList)
    if passCount < hashCount:
        passCount = ruleA(passCount, hashFile, hashCount, outList)
    if passCount < hashCount:
        passCount = ruleE(passCount, hashFile, hashCount, outList)
    if passCount < hashCount:
        passCount = ruleD(passCount, hashFile, hashCount, outList)
    

    for output in outList:
        outFile.write(output)

    # Print if there are any unmatched hashes
    if passCount < hashCount:
        print("{} hashes not found.".format(hashCount - passCount))

    # close files and finish program
    outFile.close()
    hashFile.close()
    print("Done.")

# only run if called directly
if __name__ == "__main__":
    main()
