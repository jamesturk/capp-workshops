#!/usr/bin/env python3
import argparse
from collections import Counter


def scan_text(text):
    """
    Generate summary statistics for the given text.

    Returns a dictionary with the following keys:
      * most_common_word: the most common word in the text
      * total_chars: the total number of characters in the text
      * total_words: the total number of words in the text
      * total_lines: the total number of lines in the text
    """
    counts = Counter()
    total_chars = 0
    total_words = 0
    total_lines = 0
    for word in text.split():
        counts[word] += 1
        total_chars += len(word)
        total_words += 1
        if "\n" in word:
            total_lines += 1

    return {
        "most_common_word": counts.most_common(1)[0][0],
        "most_common_count": counts.most_common(1)[0][1],
        "chars": total_chars,
        "words": total_chars,
        "lines": total_lines,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            text = f.read()
    else:
        text = input()

    stats = scan_text(text)

    print(
        "Most common word: {} ({})".format(
            stats["most_common_word"], stats["most_common_count"]
        )
    )
    print("Total chars:      {}".format(stats["chars"]))
    print("Total words:      {}".format(stats["words"]))
    print("Total lines:      {}".format(stats["lines"]))


if __name__ == "__main__":
    main()
