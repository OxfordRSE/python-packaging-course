from setuptools import setup

setup(
    name="oxrse-pypackaging-course",
    version="0.1",
    email="rse@cs.ox.ac.uk",
    url="https://github.com/OxfordRSE/python-packaging-course",
    packages=["checkpoints"],
    entry_points={
        "console_scripts": [
            "checkpoint_1 = checkpoints:checkpoint1",
            "checkpoint_2 = checkpoints:checkpoint2",
            "checkpoint_3 = checkpoints:checkpoint3"
            ]
        },
    )
