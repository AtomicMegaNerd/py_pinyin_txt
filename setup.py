from setuptools import setup, find_packages
from py_pinyin_txt.utils import getVersion

setup(
    name="py_pinyin_txt",
    version=getVersion(),
    packages=find_packages(),
    author="Chris Dunphy",
    author_email="chris@megaparsec.ca",
    description="This is a program that adds Pinyin tone marks to plain text files",
    project_urls={
        "Source Code": "https://github.com/AtomicMegaNerd/py_pinyin_txt",
    },
)