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


class TestPinyinConverted(unittest.TestCase):
    def setUp(self):
        self.test_object = PinyinConverter(test_logger)

    def test_src1_should_convert_to_res1(self):
        res = self.test_object.do_convert(SRC_1)
        self.assertEqual(RES_1, res)

    def test_standalone_numbers_ignored(self):
        res = self.test_object.do_convert(SRC_1)
        self.assertEqual(RES_1, res)
