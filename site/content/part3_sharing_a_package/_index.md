+++
title = "Sharing a package"
author = ["Thibault Lestang"]
draft = false
weight = 2004
+++

You now have a python package that you can use independently in your analyses.
This package lives somehwere in your system (the `tstools/`) directory and your can install
it in a project's virtualenv using setuptools (`pip install`).

We now look at ways your can _share_ your package with people interested in using your pkg.
This includes yourself.

Sharing means making it straightforward to both

-   Obtain the source code
-   Install and use the package

In practice this means that anyone will be able to "pip install" your package:

```shell
pip install tstools
```
