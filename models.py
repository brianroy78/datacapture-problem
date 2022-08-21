from dataclasses import dataclass
from functools import partial
from itertools import accumulate
from operator import add
from typing import Union

from core import compose
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
        return compose(
            partial(accumulate, func=calc_less_greater),
            list,
            Stats
        )(self._data)
