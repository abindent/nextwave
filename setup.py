# -*- coding: utf-8 -*-

"""
The MIT License (MIT)


Copyright (c) 2019-2021 PythonistaGuild, Sinchan Maitra

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import pathlib
import os
import re
from setuptools import setup


ROOT = pathlib.Path(__file__).parent
on_rtd = os.getenv("READTHEDOCS") == "True"

with open(ROOT/"requirements.txt") as f:
    requirements = f.read().splitlines()
    
if on_rtd:
    with open("docs/requirements_rtd.txt") as nf:
        requirements.extend(nf.read().splitlines())
        
with open(ROOT / "nextwave/__init__.py", encoding="utf-8") as f:
    VERSION = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

readme = ""
with open("README.rst") as f:
    readme = f.read()

setup(
    name="nextwave",
    author="PythonistaGuild, EvieePy, Sinchan Maitra",
    author_email='smsinchanmaitra2007@gmail.com',
    url="https://github.com/abindent/nextwave/",
    project_urls={
        "Documentation" : "https://docs.nextwave.epizy.com/",
        "Website" : "https://nextwave.epizy.com/",
        },
    version=VERSION,
    packages=["nextwave", "nextwave.ext.spotify", "nextwave.types"],
    license="MIT",
    description="A  robust and powerful Lavalink wrapper for nextcord and derivatives.",
    long_description=readme,
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)

