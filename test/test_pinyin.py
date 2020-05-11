# pylint: skip-file
# Don't waste our time linting tests

import unittest
from typing import List
from logging import Logger

from py_pinyin_txt.logging import configure_logger
from py_pinyin_txt.pinyin import PinyinConverter

test_logger: Logger = configure_logger(True)

SRC_1: List[str] = ["Ni3 hao3, wo3 xing4 Ding1."]
RES_1: List[str] = ["Nǐ hǎo, wǒ xìng Dīng."]

SRC_2: List[str] = ["Wo3 he2 2 bei1 shui3."]
RES_2: List[str] = ["Wǒ hé 2 bēi shuǐ."]

SRC_3: List[str] = [
    "Wo3 xiang3 pei3yang2 qian1bei1 de tai4du.",
    "Wo3 ye3 xiang3 bi4kai1 gao1'ao4 de tai4du!",
]
RES_3: List[str] = [
    "Wǒ xiǎng pěiyáng qiānbēi de tàidu.",
    "Wǒ yě xiǎng bìkāi gāo'ào de tàidu!",
]

SRC_4: List[str] = [
    "# Zi1liao4",
    "",
    "Wo3 xiang3 *pei3yang* qian1bei1 de tai4du.",
    "",
    "Wo3 ye3 xiang3 bi4kai1 gao1'ao4 de tai4du!",
    "",
]
RES_4: List[str] = [
    "# Zīliào",
    "",
    "Wǒ xiǎng *pěiyang* qiānbēi de tàidu.",
    "",
    "Wǒ yě xiǎng bìkāi gāo'ào de tàidu!",
    "",
]

SRC_5: List[str] = ["Xian4zai4 rang4 wo3men dou1 kao4lv4 yi2xia4 ba"]
RES_5: List[str] = ["Xiànzài ràng wǒmen dōu kàolǜ yíxià ba"]

# SRC_6: List[str] = ["chuánran3"]
# RES_6: List[str] = ["chuánrǎn"]


class TestPinyinConverted(unittest.TestCase):
    def setUp(self):
        self.test_object = PinyinConverter(test_logger)

    def test_src1_should_convert_to_res1(self):
        res = self.test_object.do_convert(SRC_1)
        self.assertEqual(RES_1, res)

    def test_standalone_numbers_ignored(self):
        res = self.test_object.do_convert(SRC_1)
        self.assertEqual(RES_1, res)

    def test_multilines_converts_properly(self):
        res = self.test_object.do_convert(SRC_3)
        self.assertEqual(RES_3, res)

    def test_blank_lines_and_markdown_should_be_preserved(self):
        res = self.test_object.do_convert(SRC_4)
        self.assertEqual(RES_4, res)

    def test_v_replaced_by_umlaut_u(self):
        res = self.test_object.do_convert(SRC_5)
        self.assertEqual(RES_5, res)


#    def test_two_consonants_in_a_row_still_works(self):
#        res = self.test_object.do_convert(SRC_6)
#        self.assertEqual(RES_6, res)
