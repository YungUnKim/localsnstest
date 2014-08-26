# -*- coding: utf-8 -*-
from kstime import kstime
from flask import render_template, request, redirect, url_for, flash, g, session, jsonify
from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy import desc
from apps import app, db
from sqlalchemy.orm.exc import NoResultFound

from apps.models import (
    Article,
    Comment,
    User
)

#
#@before request
#
# @app.before_request
# def before_request():
#     g.user_name = None

#     if 'user_id' in session:
#         g.user_name = session['user_name']
#         g.user_email = session['user_email']
#         g.user_id = session['user_id']
#
#@first page
#

@app.route('/', methods=['GET'])
def front():
    return render_template('front.html')

#
# @error Handlers
#
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500