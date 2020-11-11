import argparse
import os
import shutil


def copy_files(files_list: list, new_names=[]):
    """Copy files in FILES_LIST from .cheat/ to course/"""
    if not new_names:
        new_names = files_list
    for filename, new_filename in zip(files_list, new_names):
        cheat_file = os.path.join(".cheat", filename)
        file_to_replace = os.path.join("course", new_filename)
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
        os.path.join("analysis1", "tstools", "vis.py"),
        os.path.join("analysis1", "tstools", "moments.py"),
        os.path.join("analysis1", "tstools", "extremes.py"),
        os.path.join("analysis1", "analysis1.py"),
    ]
    copy_files(files)


def checkpoint2():
    files = [
        os.path.join("analysis1", "tstools", "__init__.py"),
        os.path.join("analysis1", "analysis1_w_init.py"),
    ]
    new_files = [
        os.path.join("analysis1", "tstools", "__init__.py"),
        os.path.join("analysis1", "analysis1.py"),
    ]
    copy_files(files, new_files)


def checkpoint3():
    if not os.path.isdir(".cheat"):
        msg = (
            "could not setup course files."
            " Are you in the course top-level directory?"
        )
        print("ERROR: " + msg)
        exit(0)

    # Not using shutil.copytree because option dir_exists_ok only
    # available since python 3.8
    for directory in ["tstools-dist", os.path.join("tstools-dist", "tstools")]:
        if not os.path.isdir(os.path.join("course", directory)):
            os.mkdir(os.path.join("course", directory))

    files = [
        os.path.join("tstools-dist", "setup.py"),
        os.path.join("tstools-dist", "tstools", "moments.py"),
        os.path.join("tstools-dist", "tstools", "vis.py"),
        os.path.join("tstools-dist", "tstools", "extremes.py"),
    ]
    copy_files(files)


def checkpoint4():
    files = [
        os.path.join("analysis2", "analysis2_centered.py"),
        os.path.join("tstools-dist", "tstools", "centered", "vis.py"),
    ]
    new_files = [
        "analysis2/analysis2_centered.py",
        "tstools-dist/tstools/vis.py",
    ]
    copy_files(files, new_files)


def main(arguments=None):
    description = (
        "Setup the course directory to a clean "
        "state prior to working on an activity."
    )
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("checkpoint_number", type=int, help="the checkpoint number")
    args = parser.parse_args(arguments)

    map_number_to_function = {
        1: checkpoint1,
        2: checkpoint2,
        3: checkpoint3,
        4: checkpoint4,
    }

    map_number_to_function[args.checkpoint_number]()


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
