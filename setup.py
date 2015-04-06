from setuptools import setup, find_packages
from glob import glob

import python_template

setup(
    name = python_template.__projectname__,
    version = python_template.__release__,
    packages = find_packages(),
    author = python_template.__authors__,
    author_email = python_template.__authoremails__,
    description = python_template.__description__,
    license = "GPLv2",
    keywords = "biopython split fasta concat",
    entry_points = {
        'console_scripts': [
        ],
    },
)
