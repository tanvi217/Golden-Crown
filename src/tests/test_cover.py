import unittest

from src.main.models.cover import Cover

class TestCover(unittest.TestCase):
    cover = Cover("ABCOFBBMUFDICCSO", "PANDA")

    def test_is_emblem_in_message(self):       
        self.assertEqual(self.cover.is_destination_emblem_in_message(), True, "PANDA in secret message")
        self.assertEqual(self.cover.is_destination_emblem_in_message(), False, "PANDA not in secret message")

    def test_emblem_hash(self):
        self.assertEqual(self.cover._cover__emblem_hash(), {"P":1, "A":2, "N":1, "D":1})

if __name__ == '__main__':
    unittest.main()