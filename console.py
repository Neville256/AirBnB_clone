#!/usr/bin/python3
"""Defines a module."""

import cmd
"""Import the cmd module."""


class HBNBCommand(cmd.Cmd):
    """ Class for our airbnb command interpreter."""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """An end of file marker."""
        return True

    def do_quit(self, stop):
        """A command to exit the program."""
        return True

    def help_quit(self):
        """Provides documentation for the quit command."""
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
