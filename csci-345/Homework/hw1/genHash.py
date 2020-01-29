import hashlib
import sys

def main():
    print("Not finished yet!")
    print("This utility helps generate hashes.\n"
    + "Select an option:\n"
    + "1: Generatea single hash")
    args = sys.argv
    if len(args) == 2:
        print(hashlib.sha256(args[1].encode("utf-8")).hexdigest())
        return

    

main()