import textwrap
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
bp = Blueprint('scenes', __name__)


@bp.route('/')
def start():
    return render_template('base.html')


# @bp.route('/scenes/welcome')
# def lets_begin():
#     tests = ['test', 'also test', 'another test']
#
#     current_scene = {
#         "title": "welcome to the game",
#         "intro": "would you like to play a game?"
#     }
#
#     return render_template("base.html", scene=current_scene)  # tests=tests)


@bp.route('/scenes/wintickets', methods=('GET', 'POST'))
def wintickets():
    tests = ['test', 'also test', 'another test']

    current_scene = {
        "title": "You FINALLY won tickets!",
        "intro": "Caller 2,465 ......... the tickets are yours!!!!!!! Finally, having no life is defnately paying off. But the rent is due....... Should you sell, or should you go????"
    }

    if request.method == 'POST':
        action = request.form['action']
        if action == "sell":
            return redirect(url_for('scenes.death'))

        elif action == "go":
            return redirect(url_for('scenes.bar'))

        else:
            return redirect(url_for('scenes.inline'))

    return render_template("base.html", scene=current_scene)


@bp.route('/scenes/sold')
def death():

    current_scene = {
        "title": "Wow....I used to think you were cool",
        "intro": "Why did you even play?\nLame.\nOh well, go back to doing whatever dumb thing you were doing in the first place."
    }

    return render_template("death.html", scene=current_scene)


@bp.route('/scenes/inline')
def inline():
    tests = ['test', 'also test', 'another test']

    current_scene = {
        "title": "Waiting in line outside the show",
        "intro": "You pull up outside the venue, where the line to get in has wrapped around the block.\nMaking your way to the VIP line, you and Kate cant help but notice all the FREAKS on parade.\nOne dodgy looking dude is making his way up the line.... he looks like Dr. Seuss and Ursula the Sea Witch had a baby.\nHe finally makes it to you... as he stands infront of you, he pulls a small bag from his pocket.......\nLOOKING TO EXPAND YOUR MIND, MAN?????\n He asks, as he waves the baggie.....\nWell, do you??"
    }

    return render_template("base.html", scene=current_scene)


@bp.route('/scenes/bar')
def bar():
    tests = ['test', 'also test', 'another test']

    current_scene = {
        "title": "",
        "intro": "You head over to the local watering hole.\nThis place is crowded...... yuck.\nThank GOD Kate\'s working behind the bar.\nShe\'s totally awesome and would LOVE to go rock the f out.... and she drives.\nThe perfect person to ask. She\'ll be getting done soon, too, so thaa----\nWOAH. Wait a minute.\nThere\'s a really hot chick at the back corner table.\nAnd DUDE.... im pretty sure she\'s making eye contact.\n(you look around just to make sure)\nYup. Definately looking at you.\nNow what\'s the play, man?? Ask Kate to go to the concert... or take your chances with \'Katia\'?"
    }
    # tests=tests)
    return render_template("base.html", scene=textwrap.dedent(current_scene))


@bp.route('/scenes/havedrink')
def havedrink_part1():
    tests = ['test', 'also test', 'anothertest']

    current_scene = {
        "title": "",
        "intro": "Kate\'s definately the wiser choice.....\nMessing with girls like Katia will have you regretting all yur life decisions.\nYou slide up and lay the tickes on the bar, waving Kate over.She looks down and squeals, \'DUDE!!!!!!! F**K YEAH IM DOWN!!!!\nI\'ll be outta here in no time.... you wanna chill and have a drink before we go?\nOr do you just wanna get going right away??\'"
    }

    return render_template("base.html", scene=current_scene)  # tests=tests)


@bp.route('/scenes/concert')
def concert():

    tests = ['test', 'also test', 'another test']
    return render_template('scenes/concert.html')  # tests=tests)
