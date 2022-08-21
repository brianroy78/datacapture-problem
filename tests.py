import unittest

from models import DataCapture
from settings import MAX_VALUE


class TestStats(unittest.TestCase):
    def test_less_input_random_disorder_numbers_return_two(self):
        capture = DataCapture()
        capture.add(5)
        capture.add(3)
        capture.add(7)
        capture.add(10)
        capture.add(55)
        stats = capture.build_stats()
        result = stats.less(7)
        self.assertEqual(result, 2)

    def test_less_input_zero_return_zero(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        result = stats.less(0)
        self.assertEqual(result, 0)

    def test_less_input_the_highest_plus_one_number_return_total(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.less(6)
        self.assertEqual(result, 5)

    def test_less_input_exact_number_return_two(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.less(3)
        self.assertEqual(result, 2)

    def test_less_input_lowest_possible_number_return_zero(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.less(0)
        self.assertEqual(result, 0)

    def test_less_input_highest_possible_number_return_total(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.less(MAX_VALUE)
        self.assertEqual(result, 5)

    def test_greater_input_random_disorder_numbers_return_two(self):
        capture = DataCapture()
        capture.add(5)
        capture.add(3)
        capture.add(7)
        capture.add(10)
        capture.add(55)
        stats = capture.build_stats()
        result = stats.greater(7)
        self.assertEqual(result, 2)

    def test_greater_input_highest_return_zero(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        result = stats.greater(9)
        self.assertEqual(result, 0)

    def test_greater_input_the_lowest_minus_one_number_return_total(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.greater(0)
        self.assertEqual(result, 6)

    def test_greater_input_exact_number_return_three(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.greater(2)
        self.assertEqual(result, 3)

    def test_greater_input_lowest_possible_number_return_total(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.greater(0)
        self.assertEqual(result, 5)

    def test_greater_input_highest_possible_number_return_zero(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.greater(MAX_VALUE)
        self.assertEqual(result, 0)

    def test_between_input_random_disorder_numbers_return_two(self):
        capture = DataCapture()
        capture.add(5)
        capture.add(3)
        capture.add(7)
        capture.add(10)
        capture.add(55)
        stats = capture.build_stats()
        result = stats.between(4, 40)
        self.assertEqual(result, 3)

    def test_between_input_exact_numbers_return_three(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.between(2, 4)
        self.assertEqual(result, 4)

    def test_between_input_lowest_and_highest_possible_numbers_return_total(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        stats = capture.build_stats()
        result = stats.between(0, MAX_VALUE)
        self.assertEqual(result, 5)
