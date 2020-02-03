import hashlib
import sys

# Really simple function that takes a string as an input and
#  prints out its sha256sum
def main():
    args = sys.argv
    if len(args) == 2:
        print(hashlib.sha256(args[1].encode("utf-8")).hexdigest())
        return

main()