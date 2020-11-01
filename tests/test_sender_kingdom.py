import unittest

from src.main.models.kingdom import Kingdom
from src.main.models.sender_kingdom import SenderKingdom

class TestSenderKingdom(unittest.TestCase):
    def setUp(self):
        self.sender = SenderKingdom("SPACE", "input.txt")

    def test_send_message(self):
        self.sender.send_message('ABCD SUMMER IS COMING', 'WATER')
        self.assertListEqual(self.sender.allies, [])

        self.sender.send_message('ABVTBTBHTBBBOBAB', 'ICE')
        self.assertListEqual(self.sender.allies, ['ICE'])

    def test_invalid_file_path(self):
        with self.assertRaises((FileNotFoundError, OSError)):
            self.sender.send_messages()

    # def test_missing_emblem_in_message(self):

    # def test_send_message_to_unkown_kingdom(self):

if __name__ == '__main__':
    unittest.main()