import unittest
from vowel import hasVowel, hasNumber

class TestSampleMethods(unittest.TestCase):
    def test_hasVowel(self):
        self.assertTrue(hasVowel("hello"))
        self.assertFalse(hasVowel("wsd"))
        self.assertFalse(hasVowel(""))

    def test_hasNumber(self):
        self.assertTrue(hasNumber("abc123"))
        self.assertFalse(hasNumber("aw"))
        self.assertFalse(hasNumber(""))

if __name__ == '__main__':
    unittest.main()