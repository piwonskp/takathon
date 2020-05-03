import logging
from inspect import getdoc, getmembers, getmodule, getmodulename, isfunction

import click

from takathon import results
from takathon.interpreter import run_tests
from takathon.output import fail, success
from takathon.tester.importer import get_modules

snd = lambda iterable: iterable[1]
fun_got_docs = lambda value: isfunction(value) and getdoc(value)


def get_functions(module):
    is_def_in_mod = lambda val: getmodule(val) == module and fun_got_docs(val)
    return map(snd, getmembers(module, is_def_in_mod))


def get_objs_to_test(path):
    return {module: get_functions(module) for module in get_modules(path)}


def test_mod(module, funs):
    return [run_tests(module, fun) for fun in funs]


def bold_fail(content):
    fail(content, bold=True)


def print_results(results):
    echo = bold_fail if results.failed else success
    echo(f"Testing finished! {results.passed} tests passed, {results.failed} failed")


def test_files(path):
    with click.progressbar(get_objs_to_test(path).items()) as bar:
        for module, funs in bar:
            test_mod(module, funs)

    print_results(results)
