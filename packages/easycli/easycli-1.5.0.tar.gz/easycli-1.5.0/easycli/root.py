import sys
import argparse
import traceback
from os import path

from .command import Command


class Root(Command):
    __completion__ = None

    def __init__(self):
        if self.__completion__:
            from .completion import Completion
            self.__arguments__.append(Completion)

        super().__init__()

        if self.__completion__:
            import argcomplete
            argcomplete.autocomplete(self._parser)

    @classmethod
    def _create_parser(self):
        return argparse.ArgumentParser(
            prog=path.basename(self.__command__ or sys.argv[0]),
            description=self.__help__
        )

    def _execute_subcommand(self, args):
        return args.func(args)

    def main(self, argv=None):
        # Parse Argument
        args = self._parser.parse_args(argv)

        if hasattr(args, 'func'):
            return self._execute_subcommand(args)
        else:
            return self(args)

    @classmethod
    def quickstart(cls, argv=None):
        return cls().main(argv)

