from typing import List
from logging import Logger

from py_pinyin_txt.data import CONVERT_DICT_1
from py_pinyin_txt.data import CONVERT_DICT_2
from py_pinyin_txt.data import CONVERT_DICT_3
from py_pinyin_txt.data import CONVERT_DICT_4
from py_pinyin_txt.data import VOWELS
from py_pinyin_txt.data import TONES


class PinyinConverter:
    """
    This class handles the core of the program.  It loads the source text file
    from disk, runs the conversion to add the pinyin tone marks, and then outputs
    the text file to the specified path.
    """

    def __init__(self, logger: Logger, infile: str, outfile: str) -> None:
        self.logger: Logger = logger
        self.infile: str = infile
        self.outfile: str = outfile
        self.text: List[str] = []
        self.converted: List[str] = []

    def convert_pinyin_text(self):
        """
        This method loads the data from the source file, runs the all-important
        _do_convert method and outputs the converted text to the destination file.
        """
        self._read_input()
        self._do_convert()
        self._write_output()

    def _do_convert(self):
        """
        This method is the meat of the program.

        This is the algorithm we are going to use:

        For each character in each line:
        1. Start a search string as a buffer.
        2. If a character is an initial consontant ignore it.
        3. If a character is a vowel or an ending consonant append it to the search string.
        4. If a character is a tone indicator (1,2,3, or 4) that's the terminator for a
        search.  in that case, add it as the final character to the search string.  Then
        search the 4, 3, 2, or 1 letter dictionaries for a match.  If a match is found
        replace it.

        Append modified lines to a new list called converted which the caller can use
        to output pinyin tone marks.
        """

        for line in self.text:
            # This string contains valid Pinyin initials and finals which
            # contain at least a vowel and a number...
            search_str: str = ""
            for char in line:
                # Add all letters that are not initial consonants to the search
                # string
                if char.isalpha():
                    if char not in VOWELS and len(search_str) == 0:
                        continue
                    search_str += char
                # All of our search strings will end with the tone indicator which
                # will be 1, 2, 3, or 4.
                elif char in TONES:
                    search_str += char
                    self.logger.debug(f"buffer = {search_str}")
                    if search_str in CONVERT_DICT_4:
                        line = line.replace(search_str, CONVERT_DICT_4[search_str], 1)
                    elif search_str in CONVERT_DICT_3:
                        line = line.replace(search_str, CONVERT_DICT_3[search_str], 1)
                    elif search_str in CONVERT_DICT_2:
                        line = line.replace(search_str, CONVERT_DICT_2[search_str], 1)
                    elif search_str in CONVERT_DICT_1:
                        line = line.replace(search_str, CONVERT_DICT_1[search_str], 1)
                    search_str = ""
                else:
                    search_str = ""
            self.logger.debug(f"Converted line: {line}")
            self.converted.append(line)

    def _read_input(self) -> None:
        """
        Read the lines in a plain text file and put each line in a list.
        """
        self.logger.info(f"Reading source pinyin from file {self.infile}")
        with open(self.infile, "r") as infile_fd:
            for line in infile_fd:
                self.text.append(line)

    def _write_output(self) -> None:
        """
        Write each converted line of text to the output file
        """
        self.logger.info(f"Writing converted pinyin to file {self.outfile}")
        with open(self.outfile, "w") as outfile_fd:
            outfile_fd.writelines(self.converted)
