from setuptools import setup, find_packages
import sys
from codecs import open
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pythoncf',
    include_package_data=True,
    packages=find_packages(),
    entry_points={'console_scripts': ['pythoncf = cf.__main__:main']},
    install_requires=['requests','prettytable','bs4','colorama','numpy','mdv','html2text','gnuplotlib','termgraph','yaspin'],
    python_requires='>=3.6',
    requires=['requests','prettytable','bs4','colorama','numpy','mdv','html2text','gnuplotlib','termgraph','yaspin'],
    version='1.1.9',
    url='https://github.com/Sudhir878786/pythoncf',
    license='MIT',
    author='Sudhir_Sharma',
    author_email='sudhirsharma@iitbhilai.ac.in',
    description='`pythoncf` is your command-line companion for all things Codeforces.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['Codeforces','cli', 'command line', 'terminal'],
)
