from setuptools import setup

setup(
    name="oxrse-pypackaging-course",
    version="0.1",
    email="rse@cs.ox.ac.uk",
    url="https://github.com/OxfordRSE/python-packaging-course",
    packages=["checkpoints"],
    entry_points={
        "console_scripts": [
            "checkpoint = checkpoints:main",
            ]
        },
    )
