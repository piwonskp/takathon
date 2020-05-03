import click


def clear_line():
    click.echo("\r\033[K", nl=False)


def fail_description_style(content, *args, **kwargs):
    return click.style(content, *args, fg="red", **kwargs)


def fail_description(content, *args, **kwargs):
    click.echo(fail_description_style(content, *args, **kwargs))


def fail_style(content, *args, **kwargs):
    return click.style(content, *args, fg="bright_red", **kwargs)


def fail(content, *args, **kwargs):
    click.echo(fail_style(content, *args, **kwargs))


def success_style(content, *args, **kwargs):
    return click.style("\n" + content, *args, fg="bright_green", bold=True, **kwargs)


def success(content, *args, **kwargs):
    click.echo(success_style(content, *args, **kwargs))
