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

### Update PATH

You may need to add Python directories to your path to make it work:

* On Windows add *\AppData\Roaming\Python\Python38\Scripts* to your PATH.
* On Mac/Linux you may need to add *$HOME/.local/bin* to your PATH.

## Usage

After installation you should be able to execute the program with the following syntax:

### Arguments

* INPUT_FILE - This is the path to the text file you wish to process.
* OUTPUT_FILE - This is the new file the program will create with the Pinyin tone 
marks.

```bash
py-pinyin-txt INPUT_FILE OUTPUT_FILE
```

### Example

```bash
py-pinyin-txt ~/Desktop/Input.md ~/Desktop/Output.md
```

## Development

To develop the project you need to use [pipenv](https://github.com/pypa/pipenv).

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
