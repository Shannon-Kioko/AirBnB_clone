#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF command to exit the program")

    def do_create(self, arg):
        """
        Create a new instance of a class, save it to the JSON file, and print the ID.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of an instance based on the class name and ID.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in [
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review",
        ]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()
            key = args[0] + "." + args[1]
            print(obj[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and ID and save the change to the JSON file.
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in [
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review",
        ]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()
            key = args[0] + "." + args[1]
            del obj[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string representations of instances of a class.
        Usage: all <class_name> or all
        """
        if arg:
            if arg not in [
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review",
            ]:
                print("** class doesn't exist **")
                return
            objects = {
                k: v
                for k, v in storage.all().items()
                if k.split(".")[0] == arg
            }
        else:
            objects = storage.all()
        print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """
        Update an instance based on the class name and ID by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in [
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review",
        ]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()
            key = args[0] + "." + args[1]
            obj_to_update = obj.get(key)
            if obj_to_update is None:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_name = args[2]
            attribute_value = args[3]
            if hasattr(obj_to_update, attribute_name):
                attribute_value = eval(attribute_value)
                setattr(obj_to_update, attribute_name, attribute_value)
                obj_to_update.save()
            else:
                print("** attribute doesn't exist **")
        except KeyError:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
