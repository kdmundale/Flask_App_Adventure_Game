import functools

from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

bp = Blueprint('hello', __name__, url_prefix='/hello')


@bp.route('/hello', methods=('GET', 'POST'))
def welcome():
    return "LETS GET TO THE DAMN SHOW!"
