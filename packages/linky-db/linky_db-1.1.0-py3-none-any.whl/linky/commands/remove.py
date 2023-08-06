from cliff.command import Command

import linky.utils.path_utils as path_utils
from linky.actions import remove


class RemoveCommand(Command):
    """
    Permanently removes / deletes a file or folder and all its links.
    Warning: This is a NON-REVERSIBLE action!
    """

    def get_parser(self, prog_name):
        parser = super(RemoveCommand, self).get_parser(prog_name)
        parser.add_argument("path", help="The file or directory to remove")
        return parser

    def take_action(self, parsed_args):
        _abs_path = path_utils.abs_path(parsed_args.path)
        remove(_abs_path)
