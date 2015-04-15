from setuptools import setup, find_packages

import runtblastx

setup(
    name = runtblastx.__projectname__,
    version = runtblastx.__release__,
    packages = find_packages(),
    author = runtblastx.__authors__,
    author_email = runtblastx.__authoremails__,
    description = runtblastx.__description__,
    license = "GPLv2",
    keywords = runtblastx.__keywords__,
    entry_points = {
        'console_scripts': [
            'runtblastx = runtblastx.runtblastx:main'
        ],
    },
)
