#!/usr/bin/python3
"""Unittest for the console"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.state import State


class Test_HBNB_command_console(unittest.TestCase):
    """"commands of console are checked"""
    def test_quit_command(self):
        """test for quit command"""
        command_result =HBNBCommand().onecmd('quit')
        self.assertTrue(command_result)

    def test_EOF_command_console(self):
        """test for EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            command_result = HBNBCommand().onecmd('EOF')
            self.assertTrue(command_result)
            self.assertEqual(f.getvalue(), '')

    def test_help_command_console(self):
        """test for help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help')
            output_patch = f.getvalue()
            help_commands = ["EOF", "all", "create", "destroy", "help", "quit", "show", "update"]
            for cmd in help_commands:
                self.assertIn(cmd, output_patch)

    def test_empty_line_command_console(self):
        """test for empty line command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_BaseModel_command_Console(self):
        """testing the creation of base mode"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            capture_output = f.getvalue()
            self.assertTrue(capture_output)

    def test_show_BaseModel_command(self):
        """tests wether or not show command shows BaseModel"""
        new_base = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(new_base.id))
            captured_output = f.getvalue()
            self.assertIn(new_base.id, captured_output)

    def test_destroy_BaseModel_command(self):
        """tests wether a given class instance is destroyed"""
        new_base = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(new_base.id))
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("show BaseModel")
            captured_output = f.getvalue()
            self.assertNotIn(new_base.id, captured_output)

    def test_all_BaseModel_command(self):
        """tests wether Basemodel class are destroyed"""
        new_base = BaseModel()
        new_base1 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            captured_output = f.getvalue()
            self.assertIn(new_base.id, captured_output)
            self.assertIn(new_base1.id, captured_output)

    def test_update_BaseModel_command(self):
        """tests wether the BaseModels is updated or not"""
        new_base = BaseModel()
        with patch ('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} created_at 123".format(new_base.id))
            captured_output = f.getvalue()
            self.assertNotIn(new_base.id, captured_output)
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("update BaseModel 123 created_at 123")
            captured_output = f.getvalue()
            self.assertEqual(captured_output, "** no instance found **\n")
            
    def test_BaseModel_all_command(self):
        """tests how base model will workin with BaseModel.all"""
        new_base = BaseModel()
        new_base1 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            captured_output = f.getvalue()
            self.assertIn(new_base.id, captured_output)
            self.assertIn(new_base1.id, captured_output)

    def test_review_all_command(self):
        """test how review all command will work with Review.all()"""
        new_review = Review()
        new_review1 = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            captured_output = f.getvalue()
            self.assertIn(new_review.id, captured_output)
            self.assertIn(new_review1.id, captured_output)
    
    def test_user_all_command(self):
        """test how user all command will work with user.all()"""
        new_user = User()
        new_user1 = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            captured_output = f.getvalue()
            self.assertIn(new_user.id, captured_output)
            self.assertIn(new_user1.id, captured_output)

    def test_user_all_command(self):
        """test how user all command will work with State.all()"""
        new_state = State()
        new_state1 = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            captured_output = f.getvalue()
            self.assertIn(new_state.id, captured_output)
            self.assertIn(new_state1.id, captured_output)

if  __name__ == "__main__":
    unittest.main()
