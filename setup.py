from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()
setup(
  name = "bababooey",
  install_requires=[],
  url = "https://replit.com/@ch1ck3n/bababooey-in-100-lines",
  version = "0.0.1",
  description = "the python program to bababooey",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = "ch1ck3n",
  author_email = "chcknch1ck3n@gmail.com",#email
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "MIT",
  packages=['bababooey'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)