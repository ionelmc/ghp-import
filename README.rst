========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-ghp-import/badge/?style=flat
    :target: https://readthedocs.org/projects/python-ghp-import
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ionelmc/python-ghp-import.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-ghp-import

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-ghp-import?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-ghp-import

.. |requires| image:: https://requires.io/github/ionelmc/python-ghp-import/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-ghp-import/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/python-ghp-import/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/python-ghp-import

.. |codecov| image:: https://codecov.io/github/ionelmc/python-ghp-import/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-ghp-import

.. |landscape| image:: https://landscape.io/github/ionelmc/python-ghp-import/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/python-ghp-import/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/79328611bdb34f74a7b08e51ce72110f.svg?style=flat
    :target: https://www.codacy.com/app/ionelmc/python-ghp-import
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/ionelmc/python-ghp-import/badges/gpa.svg
   :target: https://codeclimate.com/github/ionelmc/python-ghp-import
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/ghp-import2.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/ghp-import2

.. |downloads| image:: https://img.shields.io/pypi/dm/ghp-import2.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/ghp-import2

.. |wheel| image:: https://img.shields.io/pypi/wheel/ghp-import2.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/ghp-import2

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ghp-import2.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/ghp-import2

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ghp-import2.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/ghp-import2

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/python-ghp-import/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/python-ghp-import/


.. end-badges

A GitHub Pages import tool.

Warning
-------

This will **DESTROY** your ``gh-pages`` branch. If you love it, you'll want to
take backups before playing with this. This script assumes that `gh-pages` is
100% derivative. You should never edit files in your `gh-pages` branch by hand
if you're using this script because you will lose your work.


Installation
------------

::

    pip install ghp-import2

Usage
-----

    Usage: ghp-import [OPTIONS] DIRECTORY

    Options:
      -n          Include a .nojekyll file in the branch.
      -m MESG     The commit message to use on the target branch.
      -p          Push the branch to origin/{branch} after committing.
      -r REMOTE   The name of the remote to push to. [origin]
      -b BRANCH   Name of the branch to write to. [gh-pages]
      -h, --help  show this help message and exit

Its pretty simple. Inside your repository just run ``ghp-import $DOCS_DIR``
where ``$DOCS_DIR`` is the path to the **built** documentation. This will write a
commit to your ``gh-pages`` branch with the current documents in it.

If you specify ``-p`` it will also attempt to push the ``gh-pages`` branch to
GitHub. By default it'll just run ``git push origin gh-pages``. You can specify
a different remote using the ``-r`` flag.

You can specify a different branch with ``-b``. This is useful for user and
organization page, which are served from the ``master`` branch.

``ghp-import`` also recognizes the ``GIT_DIR`` environment variable which can be
useful for Git hooks.

License
-------

``ghp-import`` is distributed under the Tumbolia Public License. See the LICENSE
file for more information.
