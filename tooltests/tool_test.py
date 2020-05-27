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
        "output": "foo.out",
        "expected": path.join(FIXTURE_DIR, "input_expected.txt"),
        "ok": True,
    },
}


def test_case_1(tmpdir):
    print(tmpdir)
    name = "simple_case_1"
    test_case = test_cases[name]
    assert test_case is not None
    output = path.join(tmpdir, test_case["output"])
    rc = system([test_case["cmd"], test_case["input"], output])
    assert rc == test_case["ok"]
    assert cmp(output, test_case["expected"]) == True
