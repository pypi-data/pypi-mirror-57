"""Setup for the colord package."""

import setuptools


from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    author="hinzee",
    author_email="hinzee@seznam.cz",
    name='colord',
    license="MIT",
    description='colord is a python package for multiplatform colors.',
    version='v0.0.6',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hinzee/colord',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['colorama'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)