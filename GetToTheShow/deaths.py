import textwrap
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
bp = Blueprint('deaths', __name__)


@bp.route('/scenes/sold')
def death1():

    current_scene = {
        "title": "Wow....I used to think you were cool",
        "intro": "Why did you even play?\nLame.\nOh well, go back to doing whatever dumb thing you were doing in the first place."
    }

    return render_template("death.html", scene=current_scene)
