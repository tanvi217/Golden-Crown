import unittest

from src.main.controller.kingdom_to_emblem import get_emblem

class TestKingdomEmblemMapping(unittest.TestCase):

    def test_unknown_kingdom(self):
        self.assertIsNone(get_emblem("SOLAR"), "Such a kingdom does not exist")

    def test_kingdom(self):
        self.assertEqual(get_emblem("FIRE"), "Dragon", "Should be Dragon")

if __name__ == '__main__':
    unittest.main()