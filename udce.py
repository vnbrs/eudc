import glob
import os
import re

import click

from language import GoLanguage, JavaScriptLanguage, PythonLanguage, RubyLanguage

FILE_TYPES = {
    "ruby": RubyLanguage,
    "python": PythonLanguage,
    "javascript": JavaScriptLanguage,
    "go": GoLanguage,
}


@click.command()
@click.argument("search_directory", type=click.Path(resolve_path=True))
@click.option(
    "-l",
    "--languages",
    prompt="Programming languages",
    help=f"The programming languages to search for debugging calls.",
)
def cli(search_directory, languages):
    for language in languages.split(","):
        os.chdir(search_directory)
        for file in glob.glob(f"**/*.{FILE_TYPES[language].extension}", recursive=True):
            check_file(file, FILE_TYPES[language])


def check_file(file, language):
    with open(file) as file_content:
        line_number = 0
        for line in file_content:
            line_number += 1
            for check_expression in language.debugging_calls:
                if re.match(check_expression, line):
                    click.echo(f"\nFound debugging call on ", nl=False)
                    click.secho(f"{file}:", fg="red", nl=False)
                    click.secho(f"{line_number}", fg="green")
                    click.echo(line)
