def nums_to_lets():
    list = input("Enter numbers: ").split(" ")
    for num in list:
        print("{}".format(chr(int(num)+ 64)), end = "")
    print()

def every_other():
    myStr = input("Enter string to parse: ")
    shift = int(input("Enter shift: "))
    part1 = ""
    part2 = ""
    for i in range(len(myStr)):
        if i % 2 == 0:
            part1 += myStr[(i - shift) % len(myStr)]
        else:
            part2 += myStr[(i - shift) % len(myStr)]

    print()
    print(part1)
    print(part2)

def letter_frequency():
    print("Calculates frequency of characters in a string.")
    myStr = input("Enter string to parse:")

    # create list of character frequencies
    # position in list corresponds to ASCII value of letters
    charList = []
    for i in range(32,126):
        charList.append(0)
    
    for letter in myStr:
        charList[ord(letter)-32] += 1

    for i in range(len(charList)):
        if charList[i] != 0:
            print("{}: {}".format(chr(i+32), charList[i]))

every_other()