#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse

from fdiff import __version__
from fdiff.color import color_unified_diff_line
from fdiff.diff import u_diff
from fdiff.utils import file_exists


def main():  # pragma: no cover
    run(sys.argv[1:])


def run(argv):
    # ===========================================================
    # argparse command line argument definitions
    # ===========================================================
    parser = argparse.ArgumentParser(description="An OpenType table diff tool for fonts.")
    parser.add_argument(
        "--version", action="version", version="fdiff v{}".format(__version__)
    )
    parser.add_argument(
        "-c",
        "--color",
        action="store_true",
        default=False,
        help="ANSI escape code colored diff",
    )
    parser.add_argument(
        "-l", "--lines", type=int, default=3, help="Number of context lines (default 3)"
    )
    parser.add_argument("PREFILE", help="Font file path 1")
    parser.add_argument("POSTFILE", help="Font file path 2")

    args = parser.parse_args(argv)

    if not file_exists(args.PREFILE):
        sys.stderr.write(
            f"[*] ERROR: The file path '{args.PREFILE}' can not be found.{os.linesep}"
        )
        sys.exit(1)
    if not file_exists(args.POSTFILE):
        sys.stderr.write(
            f"[*] ERROR: The file path '{args.POSTFILE}' can not be found.{os.linesep}"
        )
        sys.exit(1)

    try:
        diff = u_diff(args.PREFILE, args.POSTFILE, context_lines=args.lines)
    except Exception as e:
        sys.stderr.write(
            f"[*] ERROR: During the attempt to diff the requested files the following error was encountered: {str(e)}"
        )
        sys.exit(1)

    if args.color:
        for line in diff:
            sys.stdout.write(color_unified_diff_line(line))
    else:
        sys.stdout.writelines(diff)
