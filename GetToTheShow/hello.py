from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
bp = Blueprint('test', __name__)


@bp.route('/')
def start():
    return render_template('base.html')


@bp.route('/hello/welcome')
def welcome():
    tests = ['test', 'also test', 'another test']
    return render_template('hello/welcome.html')  # tests=tests)


@bp.route('/hello/wintickets')
def wintickets():
    tests = ['test', 'also test', 'another test']
    return render_template('hello/wintickets.html')  # tests=tests)


@bp.route('/hello/inline')
def inline():
    tests = ['test', 'also test', 'another test']
    return render_template('hello/inline.html')  # tests=tests)


@bp.route('/hello/bar')
def bar():
    tests = ['test', 'also test', 'another test']
    return render_template('hello/bar.html')  # tests=tests)


@bp.route('/hello/havedrink')
def havedrink():
    tests = ['test', 'also test', 'anothertest']
    return render_template('hello/havedrink.html')  # tests=tests)


@bp.route('/hello/concert')
def concert():
    tests = ['test', 'also test', 'another test']
    return render_template('hello/concert.html')  # tests=tests)
