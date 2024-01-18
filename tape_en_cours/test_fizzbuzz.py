from fizzbuzz import fizzbuzz_element
import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz_element(3), "fizz")
