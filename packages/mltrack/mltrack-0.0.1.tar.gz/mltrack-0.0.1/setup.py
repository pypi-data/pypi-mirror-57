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
    description = "MLTrack: Track and organize your machine learning projects from the terminal",
    long_description = long_descr,
    long_description_content_type="text/markdown",
    author = "S.Shankar",
    author_email = "orthogonal.eigenvector@gmail.com",
    url = "https://bitbucket.cloud.temasek/projects/BOOT/repos/mltrack/browse",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Operating System :: Unix",
    ]
    )