=======================================================
Toy project to test executables defined in a yaml file
=======================================================

Run
--------

.. code-block:: console

    usage: test_exe_matrix [-h] [testsuite [testsuite ...]]

Without arguments, we'll test the default example file, running ```/bin/echo``` and ```/bin/sleep```.

Parametrizing tests
-------------------

Put your test suites in a yaml, like matrix.yaml (provided), or in several.

Extend the toy?
---------------

How about handling input, and even interaction (then you may like expect).

Dev: Build the package
-----------------------

Upgrade the version number in pyproject.toml and run 'poetry build' (installing poetry is a poem, sorry).
