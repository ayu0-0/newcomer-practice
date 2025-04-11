#!/usr/bin/env python3
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from pack_test.kadaie_1 import kadaie_1


def main():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="Test script for uv packaging.",
    )
    group = parser.add_mutually_exclusive_group()
    parser.add_argument(
        "-i",
        "--input1",
        help="ファイルパス",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-l",
        "--input2",
        help="残基数",
        type=int,
    )
    args = parser.parse_args()
    kadaie_1(args.input1, args.input2)


if __name__ == "__main__":
    main()
