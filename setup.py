from setuptools import setup, find_packages
from py_pinyin_txt.utils import get_version

setup(
    name="py_pinyin_txt",
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    author="Chris Dunphy",
    author_email="chris@megaparsec.ca",
    description="This is a program that adds Pinyin tone marks to plain text files",
    url="https://github.com/AtomicMegaNerd/py_pinyin_txt",
    entry_points={"console_scripts": ["py-pinyin-txt=py_pinyin_txt.__main__:main"]},
    license="BSD",
)
