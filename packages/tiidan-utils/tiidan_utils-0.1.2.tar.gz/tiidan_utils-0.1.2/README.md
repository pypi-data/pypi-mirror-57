# Overview

<table>
<tbody>
<tr class="odd">
<td>docs</td>
<td><a href="https://readthedocs.org/projects/python-tiidan-utils"><img src="https://readthedocs.org/projects/python-tiidan-utils/badge/?style=flat" alt="Documentation Status" /></a></td>
</tr>
<tr class="even">
<td>tests</td>
<td><div class="line-block"><a href="https://travis-ci.org/ionelmc/python-tiidan-utils"><img src="https://travis-ci.org/ionelmc/python-tiidan-utils.svg?branch=master" alt="Travis-CI Build Status" /></a> <a href="https://ci.appveyor.com/project/ionelmc/python-tiidan-utils"><img src="https://ci.appveyor.com/api/projects/status/github/ionelmc/python-tiidan-utils?branch=master&amp;svg=true" alt="AppVeyor Build Status" /></a> <a href="https://requires.io/github/ionelmc/python-tiidan-utils/requirements/?branch=master"><img src="https://requires.io/github/ionelmc/python-tiidan-utils/requirements.svg?branch=master" alt="Requirements Status" /></a><br />
<a href="https://codecov.io/github/ionelmc/python-tiidan-utils"><img src="https://codecov.io/github/ionelmc/python-tiidan-utils/coverage.svg?branch=master" alt="Coverage Status" /></a></div></td>
</tr>
<tr class="odd">
<td>package</td>
<td><div class="line-block"><a href="https://pypi.org/project/tiidan-utils"><img src="https://img.shields.io/pypi/v/tiidan-utils.svg" alt="PyPI Package latest release" /></a> <a href="https://pypi.org/project/tiidan-utils"><img src="https://img.shields.io/pypi/wheel/tiidan-utils.svg" alt="PyPI Wheel" /></a> <a href="https://pypi.org/project/tiidan-utils"><img src="https://img.shields.io/pypi/pyversions/tiidan-utils.svg" alt="Supported versions" /></a> <a href="https://pypi.org/project/tiidan-utils"><img src="https://img.shields.io/pypi/implementation/tiidan-utils.svg" alt="Supported implementations" /></a><br />
<a href="https://github.com/ionelmc/python-tiidan-utils/compare/v0.0.0...master"><img src="https://img.shields.io/github/commits-since/ionelmc/python-tiidan-utils/v0.0.0.svg" alt="Commits since latest release" /></a></div></td>
</tr>
</tbody>
</table>

Tiidan utils in python.

  - Free software: BSD 2-Clause License

## Installation

    pip install tiidan-utils

## Documentation

<https://python-tiidan-utils.readthedocs.io/>

## Development

To run the all tests run:

    tox

Note, to combine the coverage data from all the tox environments run:

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows</td>
<td><pre><code>set PYTEST_ADDOPTS=--cov-append
tox</code></pre></td>
</tr>
<tr class="even">
<td>Other</td>
<td><pre><code>PYTEST_ADDOPTS=--cov-append tox</code></pre></td>
</tr>
</tbody>
</table>
