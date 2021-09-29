import types
from inspect import getdoc, getmembers, getmodule, isclass, isfunction
from itertools import groupby

import click

from takathon import results
from takathon.interpreter import run_function_tests, run_method_tests
from takathon.output import fail, success
from takathon.tester.importer import get_modules

snd = lambda iterable: iterable[1]
obj_got_docs = lambda value: isclass(value) or (isfunction(value) and getdoc(value))


def get_module_objects(module):
    is_def_in_mod = lambda val: getmodule(val) == module and obj_got_docs(val)
    objects = groupby(map(snd, getmembers(module, is_def_in_mod)), type)
    return dict([(k, list(v)) for k, v in objects])


def get_objs_to_test(path):
    return {module: get_module_objects(module) for module in get_modules(path)}


def test_class(module, cls):
    methods = getmembers(cls, predicate=lambda m: isfunction(m) and getdoc(m))
    methods = filter(lambda m: m[0] != "__init__", methods)
    return [run_method_tests(module, cls, method) for _, method in methods]


def test_mod(module, objs):
    return [
        *(run_function_tests(module, fun) for fun in objs.get(types.FunctionType, [])),
        *(test_class(module, cls) for cls in objs.get(type, [])),
    ]


def bold_fail(content):
    fail(content, bold=True)


def print_results(results):
    echo = bold_fail if results.failed else success
    echo(f"Testing finished! {results.passed} tests passed, {results.failed} failed")


def test_files(path):
    with click.progressbar(get_objs_to_test(path).items()) as bar:
        for module, objs in bar:
            test_mod(module, objs)

    print_results(results)
