import sys

if __name__ == "__main__":
    if '--help' in sys.argv:
        print("Accepted: usage of --help")
    else:
        print("Not accepted: please use --help.")