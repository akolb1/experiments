from filecmp import cmp
from sys import path as syspath

syspath.insert(0,'.')

test_cases = [
    {
        "name": "simple case 1",
        "cmd": "/bin/cp",
        "input": "/tmp/foo.input",
        "output": "/tmp/foo.out",
        "expected": "/tmp/foo.expected",
    }
]

def test_tool():
    for test_case in test_cases:
        from tooltests.runtool import system
        rc = system([test_case["cmd"], test_case["input"],
                     test_case["output"]])
        assert rc == True
        assert cmp(test_case["output"], test_case["expected"]) == True
