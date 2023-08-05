# Yet Another Cache Implementation

[![Build Status](https://travis-ci.com/aabdullah-bos/yaci.svg?branch=master)](https://travis-ci.com/aabdullah-bos/yaci)

So you may be asking "Is there really a need for yet another cache
implementation?" I mean we already have:
- [functools.lru_cache (Python 3.2 or greater)](https://docs.python.org/3.7/library/functools.html#functools.lru_cache) - Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls.
- the [memoize pattern](https://dbader.org/blog/python-memoization)
- [pymemcache](https://github.com/pinterest/pymemcache) - A comprehensive, fast, pure-Python memcached client
- [DiskCache](http://www.grantjenks.com/docs/diskcache/) - An Apache2 licensed disk and file backed cache library, written in pure-Python
- [minicache](https://github.com/duboviy/minicache) - Python memory caching utilities for Python 2 and 3 versions, also PyPy.
- [pylibmc](https://github.com/lericson/pylibmc) - A Python wrapper around the libmemcached interface from TangentOrg.
- the [memento pattern](http://code.activestate.com/recipes/286132-memento-design-pattern-in-python/) - a way of saving state

The answer is no, there are plenty of caching libraries and patterns out
there and yet another one isn't necessary, so with that being said,
here is **Y**et **A**nother **C**aching **I**nterface.

## Motivation

I needed a caching interface that allowed me to change or implement
different storage backends as needed. I also wanted a caching implementation whose interface closely resembled the Python `collections.MutableMapping` interface, so that I could easily switch between dictionaries and other storage backends.

## Installing as a `pip`

To install the package run: `pip install yaci`

## Developing Using Docker

The docker directory contains a Dockerfile that can be used to build a docker image which can be used for development. See the README.md in the docker directory for more help.

## Using Pipenv

If you'd like to use Pipenv to mange this package in a development environment just run the command `pipenv install` in the top level of the repository.
