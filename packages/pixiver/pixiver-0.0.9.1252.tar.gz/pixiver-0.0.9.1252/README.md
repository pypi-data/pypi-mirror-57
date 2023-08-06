pixiver
=======

[![logo2](https://img.shields.io/badge/pypi-0.0.9.1252-blue.svg)](https://pypi.org/project/pixiver/)
[![build](https://travis-ci.org/darkchii/pixiver.svg?branch=master)](https://travis-ci.org/darkchii/pixiver)

This is a python package for get illustration on the pixiv by ajax interfaces.

Move to [Chinese Version](README-cn.md).

Install
-------

`$ pip install -U pixiver`

Quick Start
-----------

```python
from pixiver.pixiv import Pixiv

p = Pixiv(username='user', password='pw')
pw = p.works(73225282)
pw.mark()
pw.like()
pw.bookmark()
pw.save_original()
```