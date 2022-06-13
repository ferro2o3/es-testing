from flask import Blueprint, render_template, redirect, g
import toml
import os
import subprocess

exercises = Blueprint("exercises", __name__, template_folder="templates")

excluded_folders = ["__pycache__"]


def get_test_set(test_folder="./tests"):
    folders = os.listdir(test_folder)
    list_of_exercise_folders = [
        folder
        for folder in folders
        if os.path.isdir(test_folder + "/" + folder) and folder not in excluded_folders
    ]
    return list_of_exercise_folders


def get_current_set():
    config = load_config()
    if "current_test" in config:
        return config["current_test"]
    return ""


def get_test_filename(folder, exercise_set, test_number):
    cwd = os.getcwd()
    find_test = f"{cwd}/{folder}/{exercise_set}/"

    try:
        files = [
            file
            for file in os.listdir(find_test)
            if file.startswith(f"{test_number:04d}_")
        ]
    except:
        raise ValueError("File not found.")

    if len(files) == 0:
        raise ValueError("File not found.")

    return f"{cwd}/{folder}/{exercise_set}/{files[0]}"


def run_unit_tests(exercise_set, test_number):
    """
    Finds the filename of the indicated test on the indicated exercise set
    If found, runs the unit tests for the completion, if not returns the error
    """
    filename = get_test_filename("tests", exercise_set, test_number)

    run_it = [
        "pytest",
        "-x",
        "--tb=no",
        "--color=no",
        "-s",
        filename,
    ]

    result = subprocess.run(run_it, stdout=subprocess.PIPE)

    output = result.stdout.decode("utf8")

    if "FAILED" in output:
        g.last_error = output
        return False

    g.last_error = ""

    return True


def check_tests(current_set):
    number = 0

    try:

        while run_unit_tests(current_set, number):
            number += 1

    except ValueError as e:
        number = -1

    # returns the number of the last failed exercise, or -1 if there are no more exercises
    return number


def get_description(exercise_set, number):
    return "Just an exercise"


@exercises.route("/exercises", defaults={"number": 0})
@exercises.route("/exercises/<number>")
def show(number):

    number = int(number)
    current_set = get_current_set()

    if not current_set:
        return redirect("/choose-exercise-set", code=302)

    if number == 0:
        number = check_tests(current_set)

    if number == -1:
        return redirect("/exercise-set-completed", code=302)

    description = get_description(current_set, number)

    return render_template(
        "exercise.html",
        description=description,
        number=number,
        result=g.get("last_error", ""),
    )


@exercises.route("/choose-exercise-set")
def choose_set(folder="./tests"):
    test_set = get_test_set("./tests")
    return render_template("list_exercises.html", test_set=test_set)


def load_config(filename="./data/testing.toml"):
    try:
        config = toml.load(filename)
        return toml.load(filename)
    except:
        pass
    return {}


def save_config(config, filename="./data/testing.toml"):
    with open(filename, "w") as toml_file:
        toml.dump(config, toml_file)


@exercises.route("/select/<int:number>")
def selected(number, folder="./tests"):
    list_of_exercise_folders = get_test_set(folder)

    choosen = list_of_exercise_folders[number - 1]

    config = load_config()

    config["test_folder"] = folder
    config["current_test"] = list_of_exercise_folders[number - 1]

    save_config(config)

    return redirect("/exercises", code=302)


@exercises.route("/exercise-set-completed")
def completed():
    config = load_config()

    return render_template("completed_exercise.html", test_set=config["current_test"])


@exercises.route("/reset")
def reset():
    save_config({})
    return redirect("/choose-exercise-set", code=302)
