def main():
    list = input("Enter numbers: ").split(" ")
    for num in list:
        print("{}".format(chr(int(num)+ 64)), end = "")
    print()

main()