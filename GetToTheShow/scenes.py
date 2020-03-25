from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
bp = Blueprint('test', __name__)


@bp.route('/')
def start():
    return render_template('base.html')


@bp.route('/scenes/welcome')
def lets_begin():
    tests = ['test', 'also test', 'another test']

    current_scene = {
        "title": "welcome to the game",
        "intro": "would you like to play a game?"
    }

    return render_template("base.html", scene=current_scene)  # tests=tests)


@bp.route('/scenes/wintickets')
def wintickets():
    tests = ['test', 'also test', 'another test']

    current_scene = {
        "title": "You FINALLY won tickets!",
        "intro": "Caller 2,465 ......... the tickets are yours!!!!!!! Finally, having no life is defnately paying off. But the rent is due....... Should you sell, or should you go????"
    }

    return render_template("base.html", scene=current_scene)


@bp.route('/scenes/inline')
def inline():
    tests = ['test', 'also test', 'another test']

    current_scene = {
        "title": "Waiting in line outside the show",
        "intro": "You pull up outside the venue, where the line to get in has wrapped around the block. Making yur way to the VIP line, you and Kate cant help but notice all the FREAKS on parade. One dodgy looking dude is making his way up the line.... he looks like Dr. Seuss and Ursula the Sea Witch had a baby. He finally makes it to you... as he stands infront of you, he pulls a small bag from his pocket. LOOKING TO EXPAND YOUR MIND, MAN????? He asks, as he waves the baggie..... Well, do you??"
    }

    return render_template("base.html", scene=current_scene)


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
