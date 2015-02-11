#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

class {{ cookiecutter.ext_name|title }}:

    def __init__(self, app=None, *args, **kwargs):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
