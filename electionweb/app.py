#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# @file   app.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   04.03.2015
# =============================================================================
"""The web app itself."""


from flask import Flask

webapp = Flask('LHCbPCElection')


@webapp.route('/')
def index():
    """Basic landing page"""
    return '<h1>Hello, World!</h1>'

# EOF
