import hashlib
import re
import os

# a seven char word from /usr/share/dict/words which gets the first letter
# capitalized and a 1-digit number appended
def ruleA(password,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    #TODO
    dict.close()
    pass

# a ten digit password with at least one of the following special
# characters in the beginning: *,~,!,#
def ruleB(password):
    #TODO
    pass

# a five char word from /usr/share/dict/words witht he letter 'a' in it which
# gets replaced with the special character '@' and the character 'l' which is
# substituted with th number '1'
def ruleC(password,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    #TODO
    dict.close()
    pass

# any word that is made with digits up to 100 digits length
def ruleD(password):
    #TODO
    pass

# any number of chars single word from /usr/share/dict/words
def ruleE(password,dictPath="/usr/share/dict/words"):
    dict = open(dictPath,"r")
    #TODO
    dict.close()
    pass


def main():
    pass


main()
