#!/usr/bin/python3
"""Defines a module."""


import shlex
import sys
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""Import the modules."""


class HBNBCommand(cmd.Cmd):
    """ Class for our airbnb command interpreter."""
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel}

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

    def do_create(self, args):
        """Create a new instance of basemodel, saves it, and print the id."""
        storage = FileStorage()

        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            instance = eval(args[0])()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print string representation of an instance
        based on the class name and id."""
        args = shlex.split(args)
        storage = FileStorage()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
            return
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id."""
        args = shlex.split(args)
        storage = FileStorage()

        if len(args) == 0:
            print("** class name missing **")

        elif (args[0]) not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** class doesn't exist **")

        elif {args[0].args[1]} not in storage.all():
            print("** no instance found **")

        else:
            del storage.all()[args[0].args[1]]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name."""
        objects = []
        storage = FileStorage()

        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if len(args) != 0:
                if type(value) is eval(args):
                    objects.append(value)
            else:
                objects.append(value)

        print(objects)

    def do_update(self, args):
        """Updates an instance based on the class name and
        id by adding or updating attribute."""
        args = shlex.split(args)
        storage = FileStorage()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif {args[0].args[1]} not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            instance = storage.all()[{args[0].args[1]}]
            a_type = type(getattr(instance, args[2]))
            args[3] = a_type(args[3])
            setattr(instance, args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
