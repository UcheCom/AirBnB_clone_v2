#!/usr/bin/python3

"""Tests for Console"""

import unittest
from unittest.mock import patch
import os
from io import StringIO
import json
import tests
import console
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestHBNBConsole(unittest.TestCase):
    """This class is use to test console funtions"""

    @classmethod
    def setUpClass(t_cls):
        """Tests Setup"""
        t_cls.console = HBNBCommand()

    @classmethod
    def teardown(t_cls):
        """Tests tear down"""
        del t_cls.console

    def tearDown(self):
        """Deletes temp files from file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_quit(self):
        """Tests quit command"""
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("quit")
            self.assertEqual('', test.getvalue())

    def test_create(self):
        """"Tests create command"""
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("create BaseModel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("create State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("create User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("create City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("create Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("create Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("create Amenity")
            new_amenity = test.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd('create State name="California"')

    def test_all(self):
        """Tests the all cmd"""
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("all BaseMOdel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("all State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("all User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("all City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("all Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("all Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.console.onecmd("all Amenity")
            new_amenity = test.getvalue().strip()

    def test_show(self):
        """Tests show command"""
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", test.getvalue())
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("show xyz")
            self.assertEqual("** class doesn't exist **\n", test.getvalue())
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", test.getvalue())
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("show BaseModel abcdef")
            self.assertEqual("** no instance found **\n", test.getvalue())

    def test_destroy(self):
        """Tests destroy command"""
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", test.getvalue())
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("destroy State")
            self.assertEqual("** class doesn't exist **\n", test.getvalue())

    def test_count(self):
        """Tests count command"""
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("count xyz")
            self.assertEqual("0\n", test.getvalue())
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("count State")
            self.assertEqual("0\n", test.getvalue())

    def test_update(self):
        """Tests update command"""
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", test.getvalue())
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("update xyz")
            self.assertEqual("** class doesn't exist **\n", test.getvalue())
        with patch('sys.stdout', new=StringIO()) as test:
            self.console.onecmd("update State")
            self.assertEqual("** instance id missing **\n", test.getvalue())


if __name__ == '__main__':
    unittest.main()
