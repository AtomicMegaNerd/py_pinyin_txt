from typing import List
from logging import Logger

from py_pinyin_txt.pinyin import PinyinConverter


class PyPinyinTxtRunner:
    """
    This class handles the file IO and it delegates the actual conversion
    to the PinyinConverter class.
    """

    def __init__(self, logger: Logger, infile: str, outfile: str) -> None:
        self.logger: Logger = logger
        self.infile: str = infile
        self.outfile: str = outfile
        self.text: List[str] = []
        self.converted: List[str] = []

        self.converter = PinyinConverter(logger)

    def convert_pinyin_text(self):
        """
        This method loads the data from the source file, runs the all-important
        _do_convert method and outputs the converted text to the destination file.
        """
        self._read_input()
        self.converted = self.converter.do_convert(self.text)
        self._write_output()

    def _read_input(self) -> None:
        """
        Read the lines in a plain text file and put each line in a list.
        """
        self.logger.info(f"Reading source pinyin from file {self.infile}")
        with open(self.infile, "r", encoding="utf-8") as infile_fd:
            for line in infile_fd:
                self.text.append(line)

    def _write_output(self) -> None:
        """
        Write each converted line of text to the output file
        """
        self.logger.info(f"Writing converted pinyin to file {self.outfile}")
        with open(self.outfile, "w", encoding="utf-8") as outfile_fd:
            outfile_fd.writelines(self.converted)
