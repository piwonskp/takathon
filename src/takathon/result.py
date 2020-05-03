from dataclasses import dataclass, field


@dataclass
class TestResults:
    passed: int = field(default=0, init=False)
    failed: int = field(default=0, init=False)


def tests_failed(quantity):
    results.failed += quantity


def tests_passed(quantity):
    results.passed += quantity


def test_failed():
    tests_failed(1)


def test_passed():
    tests_passed(1)


results = TestResults()
