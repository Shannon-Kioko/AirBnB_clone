#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines a command interpreter with a custom prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
