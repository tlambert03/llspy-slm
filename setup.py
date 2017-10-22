# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

with open('slmgen/version.py') as f:
    exec(f.read())

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

PACKAGE_DATA = [path.join('img', 'slmgen_logo.png'),
                path.join('slmgen', 'slm_pattern_dialog.ui')]

setup(
    name='llspy-slm',
    version=__version__,
    description='Lattice Light Sheet SLM Pattern Generator',
    long_description=README,
    author='Talley Lambert',
    author_email='talley.lambert@gmail.com',
    url='https://github.com/tlambert03/llspy-slm',
    license='BSD 3-clause',
    packages=find_packages(exclude=('tests', 'docs', 'pyinstaller')),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    package_data={
        'llspy-slm': PACKAGE_DATA,
    },
    data_files=[],
    install_requires=[
        'numpy',
        'scipy',
        'numba',
        'pillow',
        'pyqt5',
    ],
    entry_points={
            'console_scripts': [
                'slmgen = slmgen.slmwindow:main',
                'slmgen-test = slmgen.slmwindow:test'
            ],
    },
)
