import pytest


collect_ignore_glob = []


def pytest_configure(config):
    if not config.option.jsonschema:
        collect_ignore_glob.append("*test_jsonschema_test_suite.py")
