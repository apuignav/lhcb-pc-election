#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# @file   app.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   04.03.2015
# =============================================================================
"""The web app itself."""


from flask import Flask, session, redirect
from flask_sso import SSO


def get_user_session_info(key):
    return session['user'].get(
        key,
        'Key `{0}` not found in user session info'.format(key)
    )


def get_user_details(fields):
    defs = [
        '<dt>{0}</dt><dd>{1}</dd>'.format(f, get_user_session_info(f))
        for f in fields
    ]
    return '<dl>{0}</dl>'.format(''.join(defs))


webapp = Flask('LHCbPCElection')
# Add a secret key for encrypting session information
webapp.secret_key = 'cH\xc5\xd9\xd2\xc4,^\x8c\x9f3S\x94Y\xe5\xc7!\x06>A'

# Map SSO attributes from ADFS to session keys under session['user']
SSO_ATTRIBUTE_MAP = {
    'ADFS_LOGIN': (True, 'username'),
    'ADFS_FULLNAME': (True, 'fullname'),
    'ADFS_PERSONID': (True, 'personid'),
    'ADFS_DEPARTMENT': (True, 'department'),
    'ADFS_EMAIL': (True, 'email')
    # There are other attributes available
    # Inspect the argument passed to the login_handler to see more
    # 'ADFS_AUTHLEVEL': (False, 'authlevel'),
    # 'ADFS_GROUP': (True, 'group'),
    # 'ADFS_ROLE': (False, 'role'),
    # 'ADFS_IDENTITYCLASS': (False, 'external'),
    # 'HTTP_SHIB_AUTHENTICATION_METHOD': (False, 'authmethod'),
}
webapp.config.setdefault('SSO_ATTRIBUTE_MAP', SSO_ATTRIBUTE_MAP)
webapp.config.setdefault('SSO_LOGIN_URL', '/login')

# This attaches the *flask_sso* login handler to the SSO_LOGIN_URL,
# which essentially maps the SSO attributes to a dictionary and
# calls *our* login_handler, passing the attribute dictionary
ext = SSO(app=webapp)

@ext.login_handler
def login(user_info):
    session['user'] = user_info
    return redirect('/')

@webapp.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@webapp.route('/')
def index():
    headings = '<h1>Hello, World!</h1>'
    if 'user' in session:
        details = get_user_details([
            'username',
            'fullname',
            'email',
            'department',
            'personid'
        ])
        button = (
            '<form action="/logout" method="get">'
            '<input type="submit" value="Log out">'
            '</form>'
        )
    else:
        details = ''
        button = (
            '<form action="/login" method="get">'
            '<input type="submit" value="Log in">'
            '</form>'
        )
    return headings + details + button


# EOF
