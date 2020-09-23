+++
title = "Uploading distributions to PyPI"
author = ["Thibault Lestang"]
draft = false
weight = 2002
+++

In the previous section you learned how to create distributions for your packages.
In this section, we look at how to share them with others, so that other people can easily install and use your packages.


## Package repositories {#package-repositories}

Let's think about distributing packages for a minute.
If you wanted to share one of your distributions (whether it's a source distribution or a wheel distribution) with a colleague, how would
you proceed?
If you both work next to each other, you could simply exchange a USB stick. If not, you can probably email the distribution, or share it _via_ a cloud host.

Although effective on a short term basis, these solutions present serious shortcomings:

-   You would have to share the distribution again each time you make a change to the package.
-   If your colleague wants a specific version (that's not the latest), you would have to check out the old version of your package and build the distribution again - unless your manually
    keep track of all your distributions.
-   Users of your package must contact you to get the distribution, and wait for you to get back to them.

These issues can be overcome by using _package repositories_. A package repository is just an index of packages hosted on distant servers, available to download from installation.
If you're using GNU/Linux, you use a package repository each time you install new software: `apt install libreoffice` is nothing but a request for the package `libreoffice` to one of
the Ubuntu package repositories.

The main reposotiry for Python is the [Python Package Index](https://pypi.org/) (PyPI).
Whenever you install a package with `pip install package`, `pip` first check than `package` isnt a directory on your machine (in which case `pip` tries to install it as a package).
If not, `pip` makes a request to PyPI and, if it exists, downloads and install package `package`.


## Publishing distributions to the test PyPI index {#publishing-distributions-to-the-test-pypi-index}

Once a package is uploaded to PyPI, it cannot easily be removed.
This is to prevent packages from disappearing without warning while other software depends on it.
To test publishing our distributions, we can use [test.pypi.org](https://test.pypi.org) instead of the regular [pypi.org](https://pypi.org/).
This is a separate database dedicated to tests and experiments.

Uploading distributions to PyPI and (TestPyPI) is a very simple process, thanks to [twine](https://twine.readthedocs.io/en/latest/), a utility for publishing Python packages on PyPI.
Installing twine is as simple as

```shell
pip install twine
```

You can now upload a distribution to to the regular PyPI (not the test one) as follows:

```shell
twine upload dist/tstools-0.1-py3-none-any.whl
```

You will be asked for your usernanme and password for PyPI. To create an account, visit <https://pypi.org/account/register/>.
If you find yourself uploading packages often, or if you are concerned about security, it is possible to authenticate to PyPI using
a token that's specific for your account, or a particular project. This token is usually configured in a `~/.pypirc` file, and allows you to authenticate
without entering your username and password every time. Note that you might want to encrypt `~/.pypirc` if concerned about security.


### Activity 7 - Publishing distributions to TestPyPI {#activity-6-publishing-distributions-to-testpypi}

1.  On PyPI (or TestPyPI), there cannot be two package with the same name. Therefore, before you upload your `tstools` package,
    you must give the project a unique name. To do so, open the `tstools-dist/setup.py` file and change the `name` entry
    in the call to the `setup` function to something unique to you, for instance:

    ```python
    name='tstools-<yourname>'
    ```
2.  Install `twine` in your `python-packaging-venv` environment

    ```shell
    pip install twine
    ```
3.  If you created some distributions in the previous sections, remove everything inside your `dist/` directory

    ```shell
    rm dist/*
    ```
4.  Create a source distribution and a wheel for your `tstools` package

    ```shell
    python setup.py sdist bdist_wheel
    ```
5.  If you don't have one, create an account on the Test PyPI index by visiting <https://pypi.org/account/register/>.
6.  Lastly, publish your distributions to the test PyPI index:

    ```shell
    twine upload --repository testpypi dist/*
    ```

    Can you find your package on [test.pypi.org](https://test.pypi.org) ?
7.  Create a new virtual environment and install your `tstools` package from the test PyPI index

    ```shell
    pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple your-package
    ```

    The above command is a bit lengthy, but it's just because we are installing from the test
    index instead of the regular one. `--index-url https://test.pypi.org/simple/` tells `pip`
    to look for the package at `test.pypi.org` instead of `pypi.org` (which is the default).
    In addition, `--extra-index-url https://pypi.org/simple` tells `pip` to looks for dependencies
    in the regular index, instead of the test one. In our case dependencies are `numpy` and `matplotlib`.

Congratulations! You just published your first Python package.

Remarks:

-   It's always a good idea to first publish your package on the test index, before
    you publish it to the real index.
-   `twine` and `pip` defaut to the real index <https://pypi.org>, so commands are really simple:

    ```shell
    twine upload <distributions> # Publish package
    pip install <package name> # Install package from pypi.org
    ```
-   You can, and _should_ publish your package each time you make a new version of it.
    All versions are stored on PyPI, and are accessible from pip.
    See the [release history for numpy](https://pypi.org/project/numpy/#history) for example.
    You could just install a specific version of numpy with:

    ```shell
    pip install numpy==1.17.5
    ```
-   Note that _you cannot_ erase a published version of your package.
    If you discover a bug in a version of your package that already has been published and want to fix it without changing the version number,
    what is known as a _post-release_, _i.e_ adding `.postX` add the end of the faulty version number.
    For instance:

    ```python
    setup(name='tstools',
          version='0.1.post1',
          ...)
    ```

    and upload your fixed package.
    This will still be considered version `0.1`, but `pip install tstools==0.1` will download
    the `0.1.post1` version.
    Note that you could publish subsequent post-releases, _i.e_ `.post2`, `.post3`...
