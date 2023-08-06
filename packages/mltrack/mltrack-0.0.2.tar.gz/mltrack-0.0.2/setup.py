# -*- coding: utf-8 -*-
 
 
"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup
 
 
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('mltrack/mltrack.py').read(),
    re.M
    ).group(1)
 
 
with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "mltrack",
    packages = ["mltrack"],
    entry_points = {
        "console_scripts": ['mlt = mltrack.mltrack:main']
        },
    version = version,
    python_requires='>=3.6',
    install_requires=[
          'jinja2',
      ],
    package_data={'mltrack': ['templates/*', 'docs_assets/*']},
    description = "MLtrack: Track your ML workflow from the terminal",
    long_description = long_descr,
    long_description_content_type="text/markdown",
    author = "S.Shankar",
    author_email = "orthogonal.eigenvector@gmail.com"
    #url = "http://gehrcke.de/2014/02/distributing-a-python-command-line-application",
    )