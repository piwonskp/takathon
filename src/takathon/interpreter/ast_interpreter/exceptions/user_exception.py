import inspect
import re

import click

from takathon.output import clear_line, fail_description_style


def def_to_doc_lineno(function):
    docs_start = re.compile(r'\)[ \t\n\r\f\v]*:\s*("""|\'\'\')\s*spec:')
    source = inspect.getsource(function)
    end_pos = docs_start.search(source).span()[1]
    return source[:end_pos].count("\n")


def docs_start_lineno(function):
    _, def_lineno = inspect.findsource(function)
    return def_lineno + def_to_doc_lineno(function)


class UserException(Exception):
    def print(self):
        for line in self.format():
            click.echo(fail_description_style(line), nl=False)
