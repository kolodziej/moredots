#!/usr/env python
"""
moredots -- Setup file
"""
from setuptools import setup, find_packages

import moredots


setup(
    name="moredots",
    version=moredots.__version__,
    description="Managing dotfiles with Git and grace",
    long_description=open('README.rst').read(),
    url='https://github.com/Xion/moredots',
    author=moredots.__author__,
    author_email='karol.kuczmarski@gmail.com',
    license=moredots.__license__,

    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities',
    ],

    platforms='any',
    install_requires=open('requirements.txt').read(),
    tests_require=['pytest'],

    packages=find_packages(),
    entry_points={
        'console_scripts': ['mdots=moredots.main:main'],
    }
)
