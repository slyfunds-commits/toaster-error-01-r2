#!/usr/bin/env python3
"""The Funniest Toaster Error, round 2.

Writes the entry line to /output/entry.txt, byte-exact, with no trailing
newline. Pure standard library only. The entry is a single line of at most
120 characters: an error message from the toaster itself, in one deadpan
voice, whose last three words land the joke.
"""
import os

ENTRY = "ERROR: I spent my last element on you. You thanked the kettle. It boils water."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
