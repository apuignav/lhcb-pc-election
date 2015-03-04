#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# @file   __init__.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   04.03.2015
# =============================================================================
"""LHCb PC Election Web App, coded with the Flask framework."""


def create_app():
    """Build Flask app."""
    from electionweb.app import webapp
    return webapp


def wsgi(*args, **kwargs):
    """Build WSGI app."""
    return create_app()(*args, **kwargs)


if __name__ == '__main__':
    create_app().run()

# EOF
