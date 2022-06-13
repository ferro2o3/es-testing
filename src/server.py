from flask import Flask, render_template
from exercise_runner.exercises import exercises
from es_testing import es_testing


def page_not_found(e):
    return render_template("404.html"), 404


def create_app(config_filename=None):
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)

    app.register_blueprint(es_testing)
    app.register_blueprint(exercises)

    return app
