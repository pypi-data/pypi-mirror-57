from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = f.read().split()

setup(
    name='temporal-cache',
    version='0.0.5',
    description='Time based function caching',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/timkpaine/temporal-cache',
    download_url='https://github.com/timkpaine/temporal-cache/archive/v0.0.5.tar.gz',
    author='Tim Paine',
    author_email='timothy.k.paine@gmail.com',
    license='Apache 2.0',
    install_requires=requires,
    extras_require={'dev': requires + ['pytest', 'pytest-cov', 'pylint', 'flake8', 'autopep8', 'mock', 'codecov']},

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='analytics tools',
    packages=find_packages(exclude=['tests', ]),
    include_package_data=True,
    zip_safe=False
)
