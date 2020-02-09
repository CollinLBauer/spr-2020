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

every_other()