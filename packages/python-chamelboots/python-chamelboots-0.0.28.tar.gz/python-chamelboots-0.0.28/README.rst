========
Overview
========


Version v0.0.28.
----------------


This is a proof of concept package. It came out of my disdain for typing any sort of HTML tag.

I often code inside of `Jupyter notebooks`_. Sometimes I want to display custom HTML inside of those notebooks.

The issue is that writing complex HTML such as a list by hand is tedious and error-prone. Template libraries do help, but they introduce their own clumsy syntax into HTML. And the templates are often very long strings that clutter the notebook. Storing the templates in files takes my mind away from the notebooks. 

Then I discovered the template library Chameleon_ that uses valid HTML as its template. Brilliant!

Though I would still have to type the templates which are HTML tags which takes me back to my original disdain of typing HTML tags.

This library addresses that issue. It also adds some utilities that I use when coding inside notebooks.

`Here is an example`_ where I used chamelboots to insert a link menu into a notebook. The links were references to anchor tags inserted into a very long cell output. It made it easier to navigate the output. *The navigation can even happen during code execution.*

.. image:: ./readme_assets/anchors.gif

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-chamelboots/badge/?style=flat
    :target: https://readthedocs.org/projects/python-chamelboots
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/dm-wyncode/python-chamelboots.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/dm-wyncode/python-chamelboots

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/dm-wyncode/python-chamelboots?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/dm-wyncode/python-chamelboots

.. |requires| image:: https://requires.io/github/dm-wyncode/python-chamelboots/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/dm-wyncode/python-chamelboots/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/dm-wyncode/python-chamelboots/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/dm-wyncode/python-chamelboots

.. |version| image:: https://img.shields.io/pypi/v/chamelboots.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/chamelboots

.. |wheel| image:: https://img.shields.io/pypi/wheel/chamelboots.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/chamelboots

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/chamelboots.svg
    :alt: Supported versions
    :target: https://pypi.org/project/chamelboots

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/chamelboots.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/chamelboots

.. |commits-since| image:: https://img.shields.io/github/commits-since/dm-wyncode/python-chamelboots/v0.0.6.svg
    :alt: Commits since latest release
    :target: https://github.com/dm-wyncode/python-chamelboots/compare/v0.0.6...master



.. end-badges


Generated with cookiecutter-pylibrary.

* Free software: BSD 2-Clause License

Installation
============

.. code-block:: bash

    pip install chamelboots

You can also install the in-development version with

.. code-block:: bash

    pip install https://github.com/dm-wyncode/python-chamelboots/archive/master.zip


It is still possible to install by cloning this repository, activating a virtual environment, and running the following:

.. code-block:: bash

   python setup.py install 



Documentation
=============


https://python-chamelboots.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

.. _Chameleon: https://chameleon.readthedocs.io/en/latest/
.. _programmatically: https://english.stackexchange.com/a/12246/159162
.. _`Python Packages index`: https://pypi.org/
.. _`Jupyter notebooks`: https://jupyter.org/
.. _`Here is an example`: https://zip.apps.selfip.com/posts/insert-a-menu-and-anchor-tags-in-a-long-jupyter-notebook-output-cell/
