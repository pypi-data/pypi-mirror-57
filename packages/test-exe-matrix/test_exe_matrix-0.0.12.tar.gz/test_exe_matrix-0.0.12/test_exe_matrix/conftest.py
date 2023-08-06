"""pytest magic
"""


import os

import yaml


def pytest_addoption(parser):
    parser.addoption(
        "--testsuite",
        help="testsuite.yaml file, see example matrix.yaml",
        default="matrix.yaml"
    )


def pytest_report_header(config):
    filename = os.path.abspath(config.option.testsuite)
    config.option.testsuite = filename
    return f"Tests from {filename}"


def pytest_generate_tests(metafunc):
    filename = metafunc.config.option.testsuite
    if "exetest" in metafunc.fixturenames:
        with open(filename, 'rb') as yamlfd:
            alltests = yaml.load(yamlfd, Loader=yaml.Loader)
            metafunc.parametrize(
                "exetest",
                [testitem for testitem in alltests]
            )
