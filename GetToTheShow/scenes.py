from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
bp = Blueprint('test', __name__)


@bp.route('/')
def start():
    return render_template('base.html')


@bp.route('/scenes/welcome')
def welcome():
    tests = ['test', 'also test', 'another test']
    return render_template('scenes/welcome.html')  # tests=tests)


@bp.route('/scenes/wintickets')
def wintickets():
    tests = ['test', 'also test', 'another test']
    return render_template('scenes/wintickets.html')  # tests=tests)


@bp.route('/scenes/inline')
def inline():
    tests = ['test', 'also test', 'another test']
    return render_template('scenes/inline.html')  # tests=tests)


@bp.route('/scenes/bar')
def bar():
    tests = ['test', 'also test', 'another test']
    return render_template('scenes/bar.html')  # tests=tests)


@bp.route('/scenes/havedrink')
def havedrink():
    tests = ['test', 'also test', 'anothertest']
    return render_template('scenes/havedrink.html')  # tests=tests)


@bp.route('/scenes/concert')
def concert():
    tests = ['test', 'also test', 'another test']
    return render_template('scenes/concert.html')  # tests=tests)
