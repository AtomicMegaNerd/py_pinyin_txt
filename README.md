# PyPinyinTxt

This Python program will take a source text file with numerical Pinyin markup (Ni3
hao3) and it will convert it to use the proper Pinyin tone marks (Nǐ Hǎo).

## Pre-Requisites

You must have Python 3.8 installed along with pip in order to use this program. You
can get Python 3.8 from [Python.org](https://python.org).

## Installation

You can install this program using pip directly from GitHub.

```bash
pip install --user git+https://github.com/AtomicMegaNerd/py_pinyin_txt.git#egg=py_pinyin_txt
```

## Usage

After installation you should be able to execute the program with the following syntax:

### Arguments

* INPUT_FILE - This is the path to the text file you wish to process.
* OUTPUT_FILE - This is the new file the program will create with the Pinyin tone 
marks.
* --version - *Optional* This will print the version of the program and exit.

```bash
py-pinyin-txt INPUT_FILE OUTPUT_FILE
```

### Example

```bash
py-pinyin-txt ~/Desktop/Input.md ~/Desktop/Output.md
```
