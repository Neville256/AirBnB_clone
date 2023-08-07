#!/usr/bin/python3
"""
Unit tests for console using Mock module from python standard library
Check console for capturing stdout into a stringIO object
"""

import os
import sys
import unittest
from unittest.mock import create_autospec, path
from io import stringIO
from console import HBNBCommand
from models import storage
from models.base_model import Basemodel
from models.user import user
from models.state import state
from models.city import city
from models.amenity import amenity
from models.place import place
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """Redirecting stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err = ["** class name missing **",
                    "** class doesnt exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    ]
        self.cls = ["basemodel",
                    "User",
                    "state",
                    "City",
                    "Place",
                    "Amenity",
                    "Review"]

    def create(self, server=None):
        """
        Redirects stdin and stdout to the mock module
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

        def last_write(self, nr=None):
            """Returns last n output lines"""
            if nr is None:
                return self.mock_stdout.write.call_args[0][0]
            return "".join(map(lambda c: c[0][0],
                               self.mock_stdout.write.call_args_list[-nr:]))

        def test_quit(self):
            """Quit command"""
            cli = self.create()
            self.asserTrue(cli.onecmd("quit"))


if __name__ == '__main__':
    unittest.main()
