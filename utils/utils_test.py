import unittest
import utils

class Test(unittest.TestCase):
    def test_state_to_word____(self):
        self.assertEqual(utils.state_to_word(0, 3), '___')

    def test_state_to_word____a(self):
        self.assertEqual(utils.state_to_word(1, 3), '__a')

    def test_state_to_word_zzz(self):
        self.assertEqual(utils.state_to_word(19682, 3), 'zzz')

    def test_state_to_word_c__(self):
        self.assertEqual(utils.state_to_word(2187, 3), 'c__')

    def test_state_to_word__jr(self):
        self.assertEqual(utils.state_to_word(288, 3), '_jr')

    def test_word_to_state_____(self):
        self.assertEqual(utils.word_to_state('___'), 0)

    def test_word_to_state____a(self):
        self.assertEqual(utils.word_to_state('__a'), 1)

    def test_word_to_state____z(self):
        self.assertEqual(utils.word_to_state('__z'), 26)

    def test_word_to_state___a_(self):
        self.assertEqual(utils.word_to_state('_a_'), 27)

    def test_word_to_state_zzz(self):
        self.assertEqual(utils.word_to_state('zzz'), 19682)

    def test_word_to_state_c__(self):
        self.assertEqual(utils.word_to_state('c__'), 2187)

    def test_word_to_state__jr(self):
        self.assertEqual(utils.word_to_state('_jr'), 288)

if __name__ == "__main__":
    unittest.main()
