import hashlib
import sys

def main():
    args = sys.argv
    if len(args) <= 1:
        print("Arguments expected.")
        return

    print(hashlib.sha256(args[1].encode("utf-8")).hexdigest())

main()