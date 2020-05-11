# PyPinyinTxt

![py_pinyin_txt CI/CD](https://github.com/AtomicMegaNerd/py_pinyin_txt/workflows/py_pinyin_txt%20CI/CD/badge.svg)

## Introcution

This Python program will take a source text file with numerical Pinyin markup (Ni3
hao3) and it will convert it to use the proper Pinyin tone marks (Nǐ Hǎo).

The rules for writing the source documents are very simple: For the pinyin
corresponding to each character put a number from 1-4 following it for the tone.
Ignore the neutral tone. Use v for ü.

## Source Pinyin Examples

* 你好(nǐhǎo) you would write: ni3hao3.
* 现在让我们都考虑一下(Xiànzài ràng wǒmen dōu kǎolǜ yíxià) write: Xian4zai4 rang4 wo3men
dou1 kao3lv4 yi2xia4 (not the v used for ü).

## Pre-Requisites

You must have Python 3.8 installed along with pip in order to use this program. You
can get Python 3.8 from [Python.org](https://python.org).

Please note that this program supports and uses the UTF-8 encoding for the plain text
files.

## Installation

You can install this program using pip directly from GitHub.

```bash
pip install --user git+https://github.com/AtomicMegaNerd/py_pinyin_txt.git#egg=py_pinyin_txt
```

### Update PATH

You may need to add Python directories to your path to make it work (replace USERNAME
with the correct name for your home directory on the Windows example):

* On Windows add *C:\Users\USERNAME\AppData\Roaming\Python\Python38\Scripts* to your PATH.
* On Mac/Linux you may need to add *$HOME/.local/bin* to your PATH.

Check the [pip documentation](https://pip.pypa.io/en/stable/) for more information.

## Usage

After installation you should be able to execute the program with the following syntax:

### Arguments

* INPUT_FILE - This is the path to the text file you wish to process.
* OUTPUT_FILE - This is the new file the program will create with the Pinyin tone.
marks.

```bash
py-pinyin-txt INPUT_FILE OUTPUT_FILE
```

### Example

```bash
py-pinyin-txt ~/Desktop/Input.md ~/Desktop/Output.md
```

## Development

To develop the project you need to use [Pipenv](https://github.com/pypa/pipenv).

```bash
pip install --user pipenv
git clone https://github.com/AtomicMegaNerd/py_pinyin_txt.git
cd py_pinyin_txt
pipenv install --dev
pipenv shell
```

To run the tests:

```bash
cd cd py_pinyin_txt
pipenv shell
python -m unittest discover
```

## Acknowledgements

This is inspired by the Pinyin Joe macros for Word and Excel, though I totally designed
this implementation myself and did not even examine the source code for those macros
as this was a programming challenge I wanted to do for fun:

[https://www.pinyinjoe.com/pinyin/pinyin_macro_faq.htm](https://www.pinyinjoe.com/pinyin/pinyin_macro_faq.htm)
