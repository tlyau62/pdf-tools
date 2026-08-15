#!/usr/bin/env python3
import argparse
from typing import TypedDict


class Args(TypedDict):
    files: list[str]
    out: str


def parse_args() -> Args:
    parser = argparse.ArgumentParser()

    parser.add_argument('--files', nargs='+')
    parser.add_argument('--out', default='merged.pdf')

    args = parser.parse_args()

    return {
        'files': args.files,
        'out': args.out
    }


if __name__ == "__main__":
    args = parse_args()

    print(args)
