import os
import shutil


def copy_files(files_list: list):
    """Copy files in FILES_LIST from .cheat/ to course/"""
    for filename in files_list:
        cheat_file = os.path.join(".cheat", filename)
        file_to_replace = os.path.join("course", filename)
        try:
            shutil.copy2(cheat_file, file_to_replace)
        except FileNotFoundError:
            msg = (
                "could not setup course files."
                " Are you in the course top-level directory?"
            )
            print("ERROR: " + msg)
            exit(0)


def checkpoint1():
    files = [
        "analysis1/tstools/vis.py",
        "analysis1/tstools/moments.py",
        "analysis1/tstools/extremes.py",
    ]
    copy_files(files)


def checkpoint2():
    files = ["analysis1/tstools/__init __.py"]
    copy_files(files)


def checkpoint3():
    if not os.is_dir(".cheat"):
        msg = (
            "could not setup course files."
            " Are you in the course top-level directory?"
        )
        print("ERROR: " + msg)
        exit(0)

    # Not using shutil.copytree because option dir_exists_ok only
    # available since python 3.8
    for directory in ["tstools-dist", os.path("tstools-dist", "tstools")]:
        if not os.is_dir(directory):
            os.mkdir(directory)

    files = [
        "tstools-dist/setup.py",
        "tstools-dist/tstools/moments.py",
        "tstools-dist/tstools/vis.py",
        "tstools-dist/tstools/extremes.py",
    ]
    copy_files(files)
