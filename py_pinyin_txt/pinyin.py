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
    This class handles the actual conversion and is written in such a way that it
    is very easy to test.
    """

    def __init__(self, logger: Logger) -> None:
        self.logger: Logger = logger

    def do_convert(self, text: List[str]) -> List[str]:
        """
        This method is the meat of the program.

        This is the algorithm we are going to use:

        For each character in each line:
        1. Start a search string as a buffer.
        2. If a character is an initial consonant ignore it.
        3. If a character is a vowel or an ending consonant append it to the search string.
        4. If a character is a tone indicator (1,2,3, or 4) that's the terminator for a
        search.  in that case, add it as the final character to the search string.  Then
        search the 4, 3, 2, or 1 letter dictionaries for a match.  If a match is found
        replace it.

        It is very important that we search the bigger dicts before the smaller ones
        because the smaller ones will also match on longer sequences and we do not want
        that.

        Append modified lines to a new list called converted which the caller can use
        to output pinyin tone marks.
        """
        converted: List[str] = []
        for line in text:
            # This string contains valid Pinyin initials and finals which
            # contain at least a vowel and a number...
            search_str: str = ""
            for char in line:
                # Add all letters that are not initial consonants to the search
                # string. Spaces and punctuation will be ignored.
                if char.isalpha():
                    if char not in VOWELS and len(search_str) == 0:
                        continue
                    search_str += char
                # All of our search strings will end with the tone indicator which
                # will be 1, 2, 3, or 4.  Note that this number may come after a vowel
                # or a consonant but we cover both cases in our four CONVERT_DICT
                # objects.
                elif char in TONES:
                    # Don't forget to append the number as they are in the keys
                    # to our dicts...
                    search_str += char

                    self.logger.debug(f"buffer = {search_str}")

                    # Make sure that we always search the bigger dicts first otherwise
                    # we will not catch the longer sequences.  The search string is
                    # compared with the keys from each dict.  If it matches a key in
                    # any of our dicts the value from that dict will be used to
                    # replace the text in the line.
                    if search_str in CONVERT_DICT_4:
                        line = line.replace(search_str, CONVERT_DICT_4[search_str], 1)
                    elif search_str in CONVERT_DICT_3:
                        line = line.replace(search_str, CONVERT_DICT_3[search_str], 1)
                    elif search_str in CONVERT_DICT_2:
                        line = line.replace(search_str, CONVERT_DICT_2[search_str], 1)
                    elif search_str in CONVERT_DICT_1:
                        line = line.replace(search_str, CONVERT_DICT_1[search_str], 1)

                    # Reset the search string when we are done...
                    search_str = ""
                else:
                    # Reset the search string if we are onto a new word...
                    search_str = ""
            self.logger.debug(f"Converted line: {line}")
            converted.append(line)

        return converted
