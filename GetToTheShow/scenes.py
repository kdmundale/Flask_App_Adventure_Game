import textwrap
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
bp = Blueprint('scenes', __name__)


@bp.route('/')
def start():
    return render_template('base.html')


def check_valid_answers(action):
    valid_answers = ['Go', 'Sell', 'go', 'sell', 'Ask Kate', 'Ask Katia', 'ask kate',
                     'ask katia', 'ask Kate', 'ask Katia', 'Have a drink', 'Have drink', 'have a drink',
                     'have drink', 'drink', 'Just go', 'just go', 'go', 'Yes', 'yes', 'Say yes', 'say yes',
                     'do it', 'Do it', 'No', 'no', 'Say no']
    while True:
        action = request.form['action']
        if action in valid_answers:
            return True
        else:
            return False


@bp.route('/scenes/wintickets', methods=('GET', 'POST'))
def wintickets():
    error = None
    tests = ['test', 'also test', 'another test']

    current_scene = {
        "title": "You FINALLY won tickets!",
        "intro": "Caller 2,465 ......... the tickets are yours!!!!!!! Finally, having no life is defnately paying off. But the rent is due....... Should you sell, or should you go????"
    }

    if request.method == 'POST':
        action = request.form['action']
        if check_valid_answers(action) == True:

            if action == "go" or "Go":
                return redirect(url_for('scenes.bar'))

            elif action == "sell" or "Sell":
                return redirect(url_for('deaths.death1'))

            else:
                error = "Not the answer we were looking for, try again!"
        else:
            error = "Not the answer we were looking for, try again!"

    return render_template("base.html", scene=current_scene, error=error)


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
        "title": "Great, tickets! But you ain't got a ride, man!!",
        "intro": "You head over to the local watering hole.\nThis place is crowded...... yuck.\nThank GOD Kate\'s working behind the bar.\nShe\'s totally awesome and would LOVE to go rock the f out.... and she drives.\nThe perfect person to ask. She\'ll be getting done soon, too, so thaa----\nWOAH. Wait a minute.\nThere\'s a really hot chick at the back corner table.\nAnd DUDE.... im pretty sure she\'s making eye contact.\n(you look around just to make sure)\nYup. Definately looking at you.\nNow what\'s the play, man?? Ask Kate to go to the concert... or take your chances with \'Katia\'?"
    }
    # tests=tests)
    return render_template("base.html", scene=current_scene)


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
