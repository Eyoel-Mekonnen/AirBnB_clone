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

if __name__ == "__main__":
    unittest.main()
