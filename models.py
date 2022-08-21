from dataclasses import dataclass
from itertools import accumulate

from settings import MAX_VALUE


@dataclass
class Data:
    less: int = 0
    greater: int = 0
    count: int = 0


class Stats:
    def __init__(self, data: list[Data]):
        self._data: list[Data] = data

    def less(self, value: int) -> int:
        """Returns the amount of number that are less than the given number"""
        return self._data[value].less

    def greater(self, value: int) -> int:
        """Returns the amount of number that are greater than the given number"""
        return self._data[value].greater

    def between(self, a: int, b: int) -> int:
        """Returns the amount of numbers between two given numbers, includes both numbers"""
        lowest, highest = (a, b) if a < b else (b, a)
        return self._data[0].greater - (self._data[lowest].less + self._data[highest].greater)


def calc_less_greater(last_data: Data, current_data: Data) -> Data:
    """Calculates the current less and greater values base on the last data"""
    current_data.less = last_data.less + last_data.count
    current_data.greater = last_data.greater - current_data.count
    return current_data


class DataCapture:
    def __init__(self):
        self._data: list[Data] = [Data() for _ in range(MAX_VALUE + 1)]
        self._total: int = 0

    def add(self, value: int):
        """Adds a new number to the data capture object"""
        self._data[value].count += 1
        self._total += 1

    def build_stats(self) -> Stats:
        """Returns the processed stats"""
        self._data[0].greater = self._total - self._data[0].count
        return Stats(list(accumulate(self._data, calc_less_greater)))
