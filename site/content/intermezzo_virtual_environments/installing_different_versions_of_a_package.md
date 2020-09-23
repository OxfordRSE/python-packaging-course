+++
title = "Installing different versions of a package"
author = ["Thibault Lestang"]
draft = false
weight = 2001
+++

In the previous section you learned how to share a package across several projects, or analyses.
However, as your package and analyses evolve asynchronously, it is likely that you will reach a point when
you'd like different analyses to use different versions of your package, or different versions of third-party
packages that your analysis rely on.

The question is then: _how to install two different versions of a same package?_
And the (short) answer is: **you cannot**.

If you type `pip install numpy==1.18`, `pip` first looks for a version
of `numpy` already installed (in the `site-packages/` directory).
If it finds a different version, say 1.19, `pip` will uninstall it and
install numpy 1.18 instead.

This limitation is very inconvenient, and is the _raison d'être_ for virtual environments, which we disuss next.
