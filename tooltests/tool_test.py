from filecmp import cmp
from os import path
from sys import path as syspath

syspath.insert(0,'.')

test_cases = {
    "simple_case_1": {
        "name": "simple_case_1",
        "cmd": path.join(".", "/bin/cp"),
        "input": "/tmp/foo.input",
        "output": "/tmp/foo.out",
        "expected": "/tmp/foo.expected",
    },
}

def test_case_1():
    test_case = test_cases["simple_case_1"]
    assert test_case is not None
    from tooltests.runtool import system
    rc = system([test_case["cmd"], test_case["input"],
                 test_case["output"]])
    assert rc == True
    assert cmp(test_case["output"], test_case["expected"]) == True
