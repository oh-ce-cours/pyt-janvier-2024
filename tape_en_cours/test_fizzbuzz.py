from fizzbuzz import fizzbuzz_element
import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz_element(3), "fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz_element(5), "buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz_element(15), "fizzbuzz")

    def test_other(self):
        self.assertEqual(fizzbuzz_element(2), "2")

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            fizzbuzz_element("2")
