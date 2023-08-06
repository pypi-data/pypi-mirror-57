import os

import pytest

DEFAULT_TESTSUITE_NAME = 'matrix.yaml'


def entrypoint():
    import argparse
    parser = argparse.ArgumentParser()
    codedir = os.path.dirname(os.path.realpath(__file__))
    default_file = os.path.join(codedir, DEFAULT_TESTSUITE_NAME)
    parser.add_argument(
        'testsuite',
        nargs='*',
        help=f"testsuite yaml file -see example {default_file}",
        default=[default_file],
    )
    args = parser.parse_args()
    options = [codedir]
    for testsuite in args.testsuite:
        pytest.main([codedir, '--testsuite', testsuite])
