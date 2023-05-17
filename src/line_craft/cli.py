#!/usr/bin/env python3

import argparse
from typing import List, Optional

from .read_write import sample_lines


def parse_arguments(arguments: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="line-craft",
        description="A simple toolkit for creating modified versions of text-based files.",
    )

    parser.add_argument("--out", required=True, type=str, help="Path to the output file")

    subparsers = parser.add_subparsers(help="Sub-command options", dest="command")

    # Subparser for the "sample" command
    parser_sample = subparsers.add_parser(
        "sample",
        help="Write a version of the file where only a random subset of lines is retained (sampled).",
    )
    parser_sample.add_argument(
        "-n", "--n-lines", type=int, help="Number of lines in target file"
    )
    parser_sample.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Pass integer to fix random seed for reproducibility (default=42)",
    )

    parser.add_argument("infile", help="Path to the input file")

    return parser.parse_args(arguments)


def main(arguments: Optional[List[str]] = None) -> None:
    # (1) Read arguments
    args = parse_arguments(arguments)

    # (2) Choose command and apply function
    if args.command == "sample":
        sample_lines(args.infile, args.out, args.n_lines, args.seed)

    return None
