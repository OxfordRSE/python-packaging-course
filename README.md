
# Table of Contents

1.  [Contents](#orge749500)
2.  [Course requirements](#org36a980e)
3.  [Getting ready for the course](#orgd20a5e2)
    1.  [How to install Python 3](#orge2e4fcb)
    2.  [Check your installation](#org8c7c538)
    3.  [Setup the python environment for the course](#org2a9bacd)
        1.  [0. Make sure you have Git installed.](#org4395fbd)
        2.  [1. Clone the course GitHub repository](#orga18da07)
        3.  [2. Create a Python virtual environment](#org2d72596)
        4.  [3. Setup the course](#org3ffd709)
        5.  [4. Deactivate your environment](#orga5bd6d7)
4.  [Building the course site](#org01ebf84)

In this workshop you will learn how to turn a couple of python scripts into
a full blown Python package. You will see how you can develop and maintain
this package independantly from your research projects and "pip install" to
reuse it across them, using virtual environments.
You will then learn the simple steps to make it possible for anyone to "pip
install" your package, automatically installing the required dependencies.


<a id="orge749500"></a>

# Contents

-   **I** Making a python package from a collection of python sripts
-   **II** Reusing package(s) across research projects
-   **III** Python virtual environments
-   **IV** Sharing your package with the world
-   **V** Overview of advanced topics


<a id="org36a980e"></a>

# Course requirements

-   A basic familiarity with Python 3
-   Python 3, pip and Git installed.


<a id="orgd20a5e2"></a>

# Getting ready for the course

The course assumes that he following software is installed on your system:

-   Python 3 (3.3 or above)
-   The `pip` package manager to upload and download Python packages.
-   The `venv` Python module to create Python virtual environments.

Not sure? Just [check your Python installation](#org8c7c538).

If you already have the above requirements satisfied, jump to [Setup the python environment for the course](https://github.com/OxfordRSE/python-packaging-course#setup-the-python-environment-for-the-course).
Otherwise, read on.


<a id="orge2e4fcb"></a>

## How to install Python 3

There are may ways of installing Python 3, depending on your
operating system, but also what you want to use Python for.
Perhaps the most straightforward way to install a "ready to go"
Python is to install [Anaconda](https://www.anaconda.com/). You can view Anaconda as a bundle
including Python itself + useful utilities (such as the `pip`
package manager) + several gigabytes worth of Python packages.  An
alternative to Anaconda is [Miniconda](https://docs.conda.io/en/latest/miniconda.html), which is essentially a
stripped version of Anaconda.  It provides a lighter Python
distribution consisting of just Python + a handful of core
utility packages.

For the purpose of this course, it really doesn't matter if you
install Miniconda or Anaconda. If you'd rather save some disk
space and go for a shorter download, we recommend you go for
Miniconda.

-   Click [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation) for instructions on how to install Miniconda/Anaconda.

If you'd rather install Python outside of Anaconda or Miniconda,
check out [our instructions](https://oxfordrse.github.io/python-packaging-course/appendix_installing_python/#install-python-3-outside-of-anacondaminiconda) on how to install Python 3 outside of
Anaconda/Miniconda.

If you encounter issues whilst installing any of the above, feel
free to get in touch by [opening an issue](https://docs.github.com/en/enterprise/2.15/user/articles/creating-an-issue) on this repository.


<a id="org8c7c538"></a>

## Check your installation

**Note**: If you installed Python withing Anaconda or Miniconda, and the
`(base)` environment is activated, replace `python3` by `python` in the following.

    python3 --version

    python3 -m pip --version

    python3 -m venv --help

If any of the three commands above results in an error, please refer to 
the [installation instructions](https://github.com/OxfordRSE/python-packaging-course#installing-python-3). If you get stuck, just [open an issue](https://docs.github.com/en/enterprise/2.15/user/articles/creating-an-issue) 
this repository and we'll help you.

If not, congratulations! Python 3 is now installed and ready to go.
One last step, let's [setup the python environment for the course](#org2a9bacd).


<a id="org2a9bacd"></a>

## Setup the python environment for the course


<a id="org4395fbd"></a>

### 0. Make sure you have Git installed.

The following commands are meant to be entered in a terminal (GNU/Linux or MacOS).

    $ git --version

If not, please install Git. On GNU/Linux Git is available *via* your package manager, for instance
on Ubuntu:

    $ sudo apt install git

On MacOS, you can use [Homebrew](https://brew.sh/) once again:

    $ brew install git

On Windows, we recommend that you use [Git for Windows](https://git-scm.com/download/win).


<a id="orga18da07"></a>

### 1. Clone the course GitHub repository

Open a terminal (or git-bash on Windows) and run the following command:

    $ git clone https://github.com/OxfordRSE/python-packaging-course.git


<a id="org2d72596"></a>

### 2. Create a Python virtual environment

Next, let's move into the course directory and create a virtual
environment.  Once this virtual environment activated, you'll work in
isolation from other Python versions installed on your machine, and
you can install any packages you want without fear or breaking any
dependencies for your other work.

**Note**: If you installed Python withing Anaconda or Miniconda, and the
`(base)` environment is activated, replace `python3` by `python` in the following.

Open a terminal (or the Anaconda prompt/command prompt if you're using Windows) and enter the following commands:

    $ cd python-packaging-course/
    $ python3 -m venv python-course-venv # just "python" for Anaconda/Miniconda
    # The following is GNU/Linux and MacOS only
    $ source python-course-venv/bin/activate # This activates the virtual environment

On windows use the following instead to activate the virtual environment.

    python-packaging-venv\Scripts\activate.bat


<a id="org3ffd709"></a>

### 3. Setup the course

Now that your Python 3 virtual environment is activated, typing
`python` at the command line will automatically call the Python 3
versions which was used to create the virtual environment (give
`python --version` a try).

Let's get the latest version of the Python package manager and install
the packages required to run the examples in the course.

    $ python -m pip install --upgrade pip
    $ python setup_course.py install


<a id="orga5bd6d7"></a>

### 4. Deactivate your environment

You're done. You can deactivate your environment with the following command:

    $ deactivate

See you at the workshop!


<a id="org01ebf84"></a>

# Building the course site

1.  Install [Hugo](https://gohugo.io/)
2.  Clone this repository
    
        $ git clone https://github.com/OxfordRSE/python-packaging-course.git
3.  Install the [Hugo Learn theme](https://learn.netlify.app/en/)
    
        $ cd python-packaging-course/site/
        $ git clone git@github.com:matcornic/hugo-theme-learn.git themes/hugo-theme-learn
4.  Build the site
    
        $ hugo server

