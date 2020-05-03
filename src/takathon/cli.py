#!/usr/bin/env python3
import logging
import os
import sys

import click
import click_log

from takathon.tester import test_files

click_log.basic_config()


@click.command(help="Test files")
@click_log.simple_verbosity_option(default=logging.getLevelName(logging.CRITICAL))
@click.argument("target", type=click.Path(), default=".")
def takathon(target):
    sys.path.insert(0, "")
    test_files(target)


if __name__ == "__main__":
    takathon()
