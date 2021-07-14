import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "flash-web-framework"
DESCRIPTION = "Python Web Framework built for learning and fun."
URL = "https://github.com/devil-cyber/flash"
EMAIL = "mani2474695@gmail.com"
AUTHOR = "Manikant Kumar"
REQUIRES_PYTHON = ">=3.8.0"
VERSION = "1.0.0"

# What packages are required for this module to be executed?
REQUIRED = [
'attrs==21.2.0',
'charset-normalizer==2.0.1',
'gunicorn==20.1.0',
'idna==3.2',
'iniconfig==1.1.1',
'Jinja2==3.0.1',
'MarkupSafe==2.0.1',
'packaging==21.0',
'parse==1.19.0',
'pluggy==0.13.1',
'py==1.10.0',
'pyparsing==2.4.7',
'pytest==6.2.4',
'requests==2.26.0',
'requests-wsgi-adapter==0.4.1',
'toml==0.10.2',
'urllib3==1.26.6',
'WebOb==1.8.7',
'whitenoise==5.2.0'

]


here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION





# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
     entrypoints={ 
       "console_scripts":[ 
           "flash=reader.api:Flash", 
       ] 
   }, 
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)