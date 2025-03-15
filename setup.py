from setuptools import setup
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='easy_trilateration',
    version='0.1.4',
    description='Easy Least-Squares trilateration using scipy',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/agusalex/Least-Squares-Trilateration',
    author='Agustin Alexander',
    author_email='agustin.c.alexander@gmail.com',
    license='MIT',
    packages=['easy_trilateration'],
    install_requires=['matplotlib',
                      'scipy'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
    ],
)
