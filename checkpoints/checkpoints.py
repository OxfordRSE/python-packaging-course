import argparse
import os
import shutil


def copy_files(files_list: list):
    """Copy files in FILES_LIST from .cheat/ to course/"""
    for filename in files_list:
        cheat_file = os.path.join(".cheat", filename)
        file_to_replace = os.path.join("course", filename)
        try:
            shutil.copy2(cheat_file, file_to_replace)
        except FileNotFoundError as error:
            print(error)
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
    files = ["analysis1/tstools/__init__.py"]
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


def main(arguments=None):
    description = (
        "Setup the course directory to a clean "
        "state prior to working on an activity."
        )
    parser = argparse.ArgumentParser(
        description=description
    )
    parser.add_argument("checkpoint_number",
                        type=int,
                        help="the checkpoint number")
    args = parser.parse_args(arguments)

    map_number_to_function = {
        1: checkpoint1,
        2: checkpoint2,
        3: checkpoint3,
    }

    map_number_to_function[args.checkpoint_number]()


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
