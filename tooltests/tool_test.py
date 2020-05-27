from filecmp import cmp
from os import path, remove
from sys import path as syspath
from runtool import system

TEST_DIR = path.dirname(path.realpath(__file__))
FIXTURE_DIR = path.join(TEST_DIR, 'data')

syspath.insert(0, TEST_DIR)

test_cases = {
    "simple_case_1": {
        "name": "simple_case_1",
        "cmd": path.join(TEST_DIR, "copier.py"),
        "input": path.join(FIXTURE_DIR, "input.txt"),
        "output": "/tmp/foo.out",
        "expected": path.join(FIXTURE_DIR, "input_expected.txt"),
        "ok": True,
    },
}


def cleanup(test_name):
    if test_name not in test_cases: return
    test_case = test_cases[test_name]
    scratch_file = test_case["output"]
    if not path.exists(scratch_file): return
    remove(scratch_file)


def test_case_1():
    name = "simple_case_1"
    test_case = test_cases[name]
    assert test_case is not None
    rc = system([test_case["cmd"], test_case["input"],
                 test_case["output"]])
    try:
        assert rc == test_case["ok"]
        assert cmp(test_case["output"], test_case["expected"]) == True
    finally:
        cleanup(name)
