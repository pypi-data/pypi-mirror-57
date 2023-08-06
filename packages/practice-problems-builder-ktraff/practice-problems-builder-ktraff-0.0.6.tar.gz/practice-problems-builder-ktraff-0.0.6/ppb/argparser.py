# MIT License

# Copyright (c) [year] [fullname]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import argparse
import os
import subprocess

from ppb.arguments import ArgList, Argument
from ppb.exceptions import NotImplementedException
from ppb.logging import setup_logger
from ppb.workers import Worker, LogWorker, NewProblemWorker, AddProblemWorker

_log = setup_logger(__name__)
_cwd = os.getcwd()


def get_author_name():
    """Retrieve a sane default for the current user's name (currently attempts to use Git)"""
    return subprocess.run(
        ['git', 'config', '--global', '--get', 'user.name'],
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8').strip()


def get_author_email():
    """Retrieve a sane default for the current user's email address (currently attempts to use Git)"""
    return subprocess.run(
        ['git', 'config', '--global', '--get', 'user.email'],
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8').strip()


class Parser:
    """Base parser for all command parser plugins."""
    args = ArgList()

    def __init__(self):
        # By default, there are no active workers associated with a parser.
        # If a parser plugin is responsible for the command issued by the user,
        # this flag can be set to True so that the worker will know that it should
        # be run
        self.worker_is_active = False

    def _activate_worker(self):
        self.worker_is_active = True

    def _add_arguments(self, parser: argparse.ArgumentParser) -> None:
        for arg in self.args:
            parser.add_argument(*arg.args, **arg.kwargs)

    def modify_parser(self, parser: argparse.ArgumentParser, subparser: argparse._SubParsersAction) -> None:
        """This is implemented here, as most parsers will need to configure a sub-parser command."""
        subparser = subparser.add_parser(self.subparser_command, help=self.subparser_help)
        self._add_arguments(subparser)
        # Add a handler to create the worker if this parser is the one that is entered by the user.
        # https://docs.python.org/2/library/argparse.html#sub-commands
        subparser.set_defaults(activate_worker=self._activate_worker)

    def create_worker(self, args: argparse.Namespace) -> Worker:
        raise NotImplementedException()


class LogParser(Parser):
    """Adds logging to CLI output"""
    args = ArgList(Argument(['--debug', '-d'], {
        'action': 'store_true',
        'help': 'Show debug logging output',
    }))

    def __init__(self):
        super().__init__()
        # The log parser is always active
        self._activate_worker()

    def modify_parser(self, parser: argparse.ArgumentParser, subparser: argparse._SubParsersAction) -> None:
        self._add_arguments(parser)

    def create_worker(self, args: argparse.Namespace) -> LogWorker:
        return LogWorker(args.debug)


class NewProblemParser(Parser):
    """Subcommand for creating a new practice problem"""
    subparser_command = 'create'
    subparser_help = 'Create a workspace for a new practice problem'
    args = ArgList(
        Argument(['problem_name'], {
            'help': 'Enter the name of your problem',
        }),
        Argument(['--language'], {
            'nargs': '+',
            'help': 'Select any number of languages in which to implement the solution',
            'choices': ['python', 'golang', 'rust'],
            'default': ['python', 'golang', 'rust'],
        }),
        Argument(['--target', '-t'], {
            'help': 'Enter the destination path for your new practice problem',
            'default': _cwd,
        }),
        Argument(['--python-version'], {
            'help': 'Enter the version of Python you would like to use with your practice problem.',
            'default': 'python3.7',
            'choices': ['python3', 'python3.6', 'python3.7'],
        }),
        Argument(['--title'], {
            'help': 'Enter the title of your new practice problem',
            'default': 'A massively helpful title',
        }),
        Argument(['--description'], {
            'help': 'Enter a description your new practice problem',
            'default': 'A massively helpful description',
        }),
        Argument(['--difficulty'], {
            'help': 'Enter the difficulty of your new practice problem (1-100)',
            'type': int,
            'default': 50,
        }),
        Argument(['--tags'], {
            'help': 'Enter any tags you would like to associate with this practice problem',
            'nargs': '+',
            'default': ['algorithms', 'data-structures'],
        }),
        Argument(['--resources'], {
            'help': 'Enter any helpful links you would like to associate with this practice problem',
            'nargs': '+',
            'default': ['http://example.com'],
        }),
        Argument(['--author-name'], {
            'help': 'Enter the name of the author for your new practice problem',
            'default': get_author_name(),
        }),
        Argument(['--author-email'], {
            'help': 'Enter the email address of the author for your new practice problem',
            'default': get_author_email(),
        }),
        Argument(['--rust-compiler-edition'], {
            'help': 'Enter the preferred compiler edition for your Rust implementation of the practice problem',
            'default': '2018',
            'choices': ['2015', '2018'],
        }),
    )

    def __init__(self):
        super().__init__()

    def create_worker(self, args: argparse.Namespace) -> NewProblemWorker:
        return NewProblemWorker(
            args.problem_name,
            args.language,
            args.target,
            args.title,
            args.description,
            args.difficulty,
            args.tags,
            args.resources,
            args.python_version,
            args.author_name,
            args.author_email,
            args.rust_compiler_edition
        )


class AddLanguageParser(Parser):
    """Subcommand for adding a language template to an existing new practice problem"""
    subparser_command = 'add'
    subparser_help = 'Add a new language to a practice problem'
    args = ArgList(
        Argument(['language'], {
            'nargs': '+',
            'help': 'Select any number of languages in which to implement the solution',
            'choices': ['python', 'golang', 'rust'],
        }),
        Argument(['--target', '-t'], {
            'help': 'Enter the destination path for your new practice problem',
            'default': _cwd,
        }),
        Argument(['--python-version'], {
            'help': 'Enter the version of Python you would like to use with your practice problem.',
            'default': 'python3.7',
            'choices': ['python3', 'python3.6', 'python3.7'],
        }),
        Argument(['--rust-compiler-edition'], {
            'help': 'Enter the preferred compiler edition for your Rust implementation of the practice problem',
            'default': '2018',
            'choices': ['2015', '2018'],
        }),
    )

    def __init__(self):
        super().__init__()

    def create_worker(self, args: argparse.Namespace) -> NewProblemWorker:
        return AddProblemWorker(
            args.language,
            args.target,
            args.python_version,
            args.rust_compiler_edition,
        )
