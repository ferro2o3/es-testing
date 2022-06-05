from flask import Blueprint, render_template, redirect

import os
import subprocess

# from flask import current_app as app

es_testing = Blueprint("es_testing", __name__, template_folder="templates")


@es_testing.route("/")
def show():

    return redirect("/exercises", code=302)
