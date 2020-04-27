"""
PyPinyinTxt

This is the main module that parses the command-line arguments, configures the logging
and the calls into the meat of the code.
"""

import argparse
import sys
from logging import Logger

from py_pinyin_txt.runner import PyPinyinTxtRunner
from py_pinyin_txt.logging import configure_logger
from py_pinyin_txt.utils import getVersion


def main(args=None) -> None:
    """
    This is the main subroutine.
    """

    parser = argparse.ArgumentParser(prog="PyPinyinTxt")

    parser.add_argument(
        "infile", type=str, help="This is the input file that contains the source text",
    )
    parser.add_argument(
        "outfile",
        type=str,
        help="THis is the output file that will contain our converted Pinyin",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="This flag enables debug logging to aid development",
    )

    args = parser.parse_args()

    logger: Logger
    if args.debug:
        logger = configure_logger(True)
    else:
        logger = configure_logger()

    try:
        converter = PyPinyinTxtRunner(logger, args.infile, args.outfile)
        converter.convert_pinyin_text()
        logger.info("Program completed conversion without errors.")
    except Exception as err:
        logger.error(f"Something went wrong: {err}")
        sys.exit(-1)


if __name__ == "__main__":
    main()
