import unittest
from romanToInt import Solution

class TestRomanToInt(unittest.TestCase):
    def test_simple_cases(self):
        s = Solution()
        self.assertEqual(s.romanToInt("III"), 3)

    def test_subtractive_cases(self):
        s = Solution()
        self.assertEqual(s.romanToInt("IV"), 4)
        self.assertEqual(s.romanToInt("IX"), 9)

    def test_complex_case(self):
        s = Solution()
        self.assertEqual(s.romanToInt("MCMXCIV"), 1994)

if __name__ == '__main__':
    unittest.main()
