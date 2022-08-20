import unittest

from models import DataCapture


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
