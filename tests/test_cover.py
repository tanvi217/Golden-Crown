import unittest

from src.main.models.cover import Cover

class TestCover(unittest.TestCase):
    cover1 = Cover("ABCOFBBMUFDICCSO", "PANDA")
    cover2 = Cover('ABCD SUMMER IS COMING', 'WATER')

    def test_is_emblem_in_message(self):       
        self.assertTrue(self.cover1.is_destination_emblem_in_message(), "PANDA in secret message")
        self.assertFalse(self.cover2.is_destination_emblem_in_message(), "PANDA not in secret message")

    def test_emblem_hash(self):
        self.assertDictEqual(self.cover1._Cover__emblem_hash(), {"P":1, "A":2, "N":1, "D":1})
        self.assertDictEqual(self.cover2._Cover__emblem_hash(), {"W":1, "A":1, "T":1, "E":1, "R":1})

if __name__ == '__main__':
    unittest.main()