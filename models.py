from dataclasses import dataclass
from functools import partial
from itertools import accumulate
from operator import add

from core import compose
from settings import MAX_VALUE


@dataclass
class Data:
    less: int


class Stats:
    def __init__(self, data: list[Data]):
        self._data: list[Data] = data

    def less(self, value: int) -> int:
        """Returns the amount of number that are less than the given number"""
        return self._data[value].less


class DataCapture:
    def __init__(self):
        self._data: list[int] = [0] * MAX_VALUE

    def add(self, value: int):
        """Adds a new number to the data capture object"""
        self._data[value] += 1

    def build_stats(self) -> Stats:
        """Returns the processed stats"""
        return compose(
            partial(accumulate, func=add, initial=0),
            partial(map, Data),
            list,
            Stats
        )(self._data)
