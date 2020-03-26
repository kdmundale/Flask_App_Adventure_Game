import textwrap
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
bp = Blueprint('deaths', __name__)


@bp.route('/scenes/death1')
def death1():

    current_scene = {
        "title": "Wow....I used to think you were cool",
        "intro": "Why did you even play?\nLame.\n..................................................................................\nOh well, go back to doing whatever dumb thing you were doing in the first place."
    }

    return render_template("death.html", scene=current_scene)

@bp.route('/scenes/death2')
def death2():

    current_scene = {
        "title": "",
        "intro": "COULD ANYONE BLAME YOU?!?!?!\n..................................................................................\nI mean, it\'s not every day you get the opportunity to ask out such an exotic creature. Maybe she\'s a fan of the band, too.\n..................................................................................\nYou sit down beside Katia, and happily accept the drink(s) she starts puttingin front of you.\n..................................................................................\nSuddenly, it all goes black.\n..................................................................................\n\'Why am I so cold?\'... you ask yourself as you slowly come too.\n..................................................................................\nLooking around, the bathroom clearly belongs to one of those crappy motels by the highway.\n..................................................................................\nFreezing, you begin to realize you\'re floating in a tub of ice... \n..................................................................................\n\'Why does my side hurt? Where are my clothes????\'\n..................................................................................\nYou look down, and see the sutures accross your abdomin.....\n..................................................................................\nMY MOTHER F**ING KIDNEY!!!"
    }
    return render_template("death.html", scene=current_scene)
