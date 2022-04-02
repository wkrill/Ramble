# python setup.py develop    # for development
# python setup.py install    # for final install
from setuptools import setup


CLASSIFIERS = '''\
Programming Language :: Python :: 3.9 :: 3.10
Topic :: Software Development
Operating System :: MacOS
'''

DISTNAME = 'ramble'
AUTHOR = 'William Krill'
AUTHOR_EMAIL = 'williamkrill1k@gmail.com'
DESCRIPTION = 'A package to generate sentences based on word rules.'
LICENSE = 'MIT'
README = 'A package to generate sentences based on word rules.'

VERSION = '0.1.0'
ISRELEASED = False

PYTHON_MIN_VERSION = '3.9'
PYTHON_MAX_VERSION = '3.9'
PYTHON_REQUIRES = f'>={PYTHON_MIN_VERSION}, <={PYTHON_MAX_VERSION}'

INSTALL_REQUIRES = []

PACKAGES = [
    'ramble',
    'tests'
]

metadata = dict(
    name=DISTNAME,
    version=VERSION,
    long_description=README,
    packages=PACKAGES,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    classifiers=[CLASSIFIERS],
    license=LICENSE
)


def setup_package() -> None:
    setup(**metadata)
