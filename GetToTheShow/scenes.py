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
    valid_answers = ['Go', 'Sell', 'go', 'sell', 'Ask Kate', 'Ask Katia', 'ask kate', 'kate', 'katia',
                     'ask katia', 'ask Kate', 'ask Katia', 'Have a drink', 'Have drink', 'have a drink',
                     'have drink', 'drink', 'Just go', 'just go', 'go', 'Yes', 'yes', 'Say yes', 'say yes',
                     'do it', 'Do it', 'No', 'no', 'Say no', 'Say thanks', 'say thanks', 'Thank kate', 'thanks',
                     'thank kate', 'pretend nothing happened', 'Pretend nothing happened', 'nothing', 'nothing happened',
                     'act like nothing happened', 'Act like nothing happened']
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
        "intro": "\'Caller 2,465 ......... the tickets are YOURS!!!!!!!\'\n..................................................................................\nFinally, having no life is defnately paying off, and countless calls to the local radio station has landed you with 2 tickets to the GREATEST ROCK SHOW EVER, tonight!\n..................................................................................\nBut the rent is due, and missing work \'cause you went too hard at the show ISN\'T a good excuse\n..................................................................................\nShould you sell, or should you go????"
    }

    if request.method == 'POST':
        action = request.form['action']
        if check_valid_answers(action) == True:

            action = request.form['action']

            if action == "go" or action == "Go":
                return redirect(url_for('scenes.bar'))

            elif action == "sell" or action == "Sell":
                return redirect(url_for('deaths.death1'))

            else:
                error = "Not the answer we were looking for, try \'Go\' or \'Sell\'!"
        else:
            error = "Not the answer we were looking for, try again!"

    return render_template("base.html", scene=current_scene, error=error)


@bp.route('/scenes/inline', methods=('GET', 'POST'))
def inline():
    error = None
    tests = ['test', 'also test', 'another test']

    current_scene = {
        "title": "After a short drive, and some warm-up jamming in the car....",
        "intro": "You pull up outside the venue, where the line to get in has wrapped around the block.\n..................................................................................\nMaking your way to the VIP line, you and Kate cant help but notice all the FREAKS on parade.\n..................................................................................\nOne dodgy looking dude is making his way up the line.... he looks like Dr. Seuss and Ursula the Sea Witch had a baby.\n..................................................................................\nHe finally makes it to you... and as he stands infront of you, he pulls a small bag from his pocket.......\n..................................................................................\n\'LOOKING TO EXPAND YOUR MIND, MAN?????\'\n He asks, as he waves the baggie.\n..................................................................................\nWell, are you??"
    }

    return render_template("base.html", scene=current_scene)


@bp.route('/scenes/bar', methods=('GET', 'POST'))
def bar():
    error = None
    tests = ['test', 'also test', 'another test']

    current_scene = {
        "title": "Great, tickets! But you ain't got a ride, man!!",
        "intro": "You head over to the local watering hole.\n..................................................................................\nThis place is crowded. Yuck.\n..................................................................................\nThank GOD Kate\'s working behind the bar. She\'s totally awesome and would LOVE to go rock the F**K out.... and she drives.\n..................................................................................\nThe perfect person to ask. \n..................................................................................\nShe\'ll be getting done soon, too, so thaa----\n..................................................................................\nWOAH. Wait a minute.\n..................................................................................\nThere\'s a really hot chick at the back corner table.\nAnd DUDE.... im pretty sure she\'s making eye contact.\n..................................................................................\n(you look around just to make sure)\n..................................................................................\nYup. Definately looking at you.\n..................................................................................\nNow what\'s the play, man?? Ask Kate to go to the concert... or take your chances with mystery woman \'Katia\'?"
    }

    if request.method == 'POST':
        action = request.form['action']
        if check_valid_answers(action) == True:

            if action == "Ask Kate" or action =="ask kate" or action == "Kate" or action == "kate":
                return redirect(url_for('scenes.havedrink1'))

            elif action == "Ask Katia" or action == "ask katia" or action == "Katia" or action == "katia":
                return redirect(url_for('deaths.death2'))

            else:
                error = "Not the answer we were looking for, try \'Ask Kate\' or \'Ask Katia\'!"
        else:
            error = "Not the answer we were looking for, try again!"

    return render_template("base.html", scene=current_scene, error=error)


@bp.route('/scenes/havedrink1', methods=('GET', 'POST'))
def havedrink1():
    error = None
    tests = ['test', 'also test', 'anothertest']

    current_scene = {
        "title": "",
        "intro": "Kate\'s definately the wiser choice\n..................................................................................\nMessing with girls like Katia will have you regretting all your life decisions.\n..................................................................................\nYou slide up and lay the tickes on the bar, waving Kate over.\n..................................................................................\nShe looks down and squeals, \'DUDE!!!!!!! F**K YEAH IM DOWN!!!!\nI\'ll be outta here in no time.... you wanna chill and have a drink before we go?\nOr do you just wanna get going right away??\'"
    }
    if request.method == 'POST':
        action = request.form['action']
        if check_valid_answers(action) == True:

            if action == "Have a drink" or action == "have a drink" or action == "Drink" or action =="drink":
                return redirect(url_for('scenes.havedrink2'))

            elif action == "Go" or action == "go" or action == "just go" or action == "Just go":
                return redirect(url_for('scenes.inline'))

            else:
                error = "Not the answer we were looking for, try \'Have a drink\' or \'Just go\'"
        else:
            error = "Not the answer we were looking for, try again!"

    return render_template("base.html", scene=current_scene, error=error)  # tests=tests)


@bp.route('/scenes/havedrink2', methods=('GET', 'POST'))
def havedrink2():
    error = None
    tests = ['test', 'also test', 'anothertest']

    current_scene = {
        "title": "Why not enjoy a drink? You deserve it!",
        "intro": "You pull up a barstool and wait for Kate to come around.\nThe bartender comes over with a drink,\'Someone bought this for you.\' \n..................................................................................\n\'WELL SHIT, TODAY IS YOUR LUCKY DAY!!!!\n..................................................................................\nWithout even hesitating... you take a huge sip.\n..................................................................................\nCrap.\n..................................................................................\nThe room starts to spin.\nAs the lights begin to fade.... you see a figure approach.\n..................................................................................\n KATIA.\n..................................................................................\n'Goodnight, friend.....\' she whisperes.\n..................................................................................\nYou come too in the front seat of Katie\'s car.\n..................................................................................\n YET AGAIN, she\'s done you a solid.SAVED YOUR LIFE.\n..................................................................................\nShe kicked Katia\'s ass and got you on the road to the concert.\n..................................................................................\nNEVER UNDERESTIMATE A GOOD BARTENDER.\n..................................................................................\nDo you say thanks, or out of embarassment pretend nothing happened?"
    }
    if request.method == 'POST':
        action = request.form['action']
        if check_valid_answers(action) == True:

            if action == "Say thanks" or action == "say thanks" or action == "Thank kate" or action == "thank kate" or action == "thanks":
                return redirect(url_for('scenes.inline'))

            elif action == "pretend nothing happened" or action == "Pretend nothing happened" or action == "nothing" or action == "nothing happened" or action == "act like nothing happened" or action == "Act like nothing happened":
                return redirect(url_for('deaths.death3'))

            else:
                error = "Not the answer we were looking for, try \'Nothing happened\' or \'Say thanks\'!"
        else:
            error = "Not the answer we were looking for, try again!"

    return render_template("base.html", scene=current_scene, error=error)


def concert():

    tests = ['test', 'also test', 'another test']
    return render_template('scenes/concert.html')  # tests=tests)
