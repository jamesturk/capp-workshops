import argparse


def main():
    # wc takes the following arguments:
    # -l: count the number of lines
    # -w: count the number of words
    # -c: count the number of characters

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", action="store_true")
    parser.add_argument("-w", action="store_true")
    parser.add_argument("-c", action="store_true")
    parser.add_argument("file", nargs="?")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            text = f.read()
    else:
        text = input()

    if args.l:
        print(len(text.splitlines()))
    if args.w:
        print(len(text.split()))
    if args.c:
        print(len(text))

    pass
