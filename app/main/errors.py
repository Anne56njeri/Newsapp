from flask import render_template
from . import main

@main.app_errorhandler(404)
def four(errors):
    return render_template('four.html'),404
