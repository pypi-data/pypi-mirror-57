#! /usr/bin/env python3
import sys


def introduction(name: str):
    print(f"Hello World!\n\tLet me introduce: {name}")


if __name__ == '__main__':
    inputs = sys.argv[1:]
    if inputs:
        run_simple(" ".join(inputs))
    else:
        print("🙄 I require inputs!")

