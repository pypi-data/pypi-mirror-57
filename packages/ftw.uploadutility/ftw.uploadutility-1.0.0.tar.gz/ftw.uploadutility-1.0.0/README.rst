.. contents:: Table of Contents


Introduction
============

Port of "ZPublisher.HTTPRequest.FileUpload" utility from plone 5 to plone 4.


Compatibility
-------------

Plone 4.3.x


Installation
============

- Add the package to your buildout configuration:

::

    [instance]
    eggs +=
        ...
        ftw.uploadutility


Development
===========

1. Fork this repo
2. Clone your fork
3. Shell: ``ln -s development.cfg buildout.cfg``
4. Shell: ``python bootstrap.py``
5. Shell: ``bin/buildout``

Run ``bin/test`` to test your changes.

Or start an instance by running ``bin/instance fg``.


Links
=====

- Github: https://github.com/4teamwork/ftw.uploadutility
- Issues: https://github.com/4teamwork/ftw.uploadutility/issues
- Pypi: http://pypi.python.org/pypi/ftw.uploadutility


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.uploadutility`` is licensed under GNU General Public License, version 2.
