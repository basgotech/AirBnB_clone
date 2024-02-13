import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, function, *args):
        function(*args)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_nothing(self, mock_stdout):
        self.assert_stdout("", self.hbnb_command.do_nothing, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        self.assertTrue(self.hbnb_command.do_quit(""))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        self.assertTrue(self.hbnb_command.do_EOF(""))

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.assert_stdout("", self.hbnb_command.emptyline, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        self.assert_stdout("** class name missing **", self.hbnb_command.do_create, "")
        self.assert_stdout("** class doesn't exist **", self.hbnb_command.do_create, "NonExistentClass")
        self.assert_stdout("", self.hbnb_command.do_create, "BaseModel")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        self.assert_stdout("** class name missing **", self.hbnb_command.do_show, "")
        self.assert_stdout("** class doesn't exist **", self.hbnb_command.do_show, "NonExistentClass 123")
        self.assert_stdout("** instance id missing **", self.hbnb_command.do_show, "BaseModel")
        with patch('console.storage.reload'):
            with patch('console.storage.all', return_value={'BaseModel.123': 'instance_data'}):
                self.assert_stdout("instance_data", self.hbnb_command.do_show, "BaseModel 123")

    # Add similar tests for other commands like do_destroy, do_all, do_update, etc.

if __name__ == '__main__':
    unittest.main()

