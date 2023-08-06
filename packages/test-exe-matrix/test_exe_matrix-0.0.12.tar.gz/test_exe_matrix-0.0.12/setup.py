# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['test_exe_matrix']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.2', 'pytest==5.3.1']

entry_points = \
{'console_scripts': ['test_exe_matrix = test_exe_matrix.main:entrypoint']}

setup_kwargs = {
    'name': 'test-exe-matrix',
    'version': '0.0.12',
    'description': '',
    'long_description': "=======================================================\nToy project to test executables defined in a yaml file\n=======================================================\n\nRun\n--------\n\n.. code-block:: console\n\n    usage: test_exe_matrix [-h] [testsuite [testsuite ...]]\n\nWithout arguments, we'll test the default example file, running ```/bin/echo``` and ```/bin/sleep```.\n\nParametrizing tests\n-------------------\n\nPut your test suites in a yaml, like matrix.yaml (provided), or in several.\n\nExtend the toy?\n---------------\n\nHow about handling input, and even interaction (then you may like expect).\n\nDev: Build the package\n-----------------------\n\nUpgrade the version number in pyproject.toml and run 'poetry build' (installing poetry is a poem, sorry).\n",
    'author': 'Feth AREZKI',
    'author_email': 'text_exe_matrix@tuttu.info',
    'url': 'https://framagit.org/feth/test_exe_matrix',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
