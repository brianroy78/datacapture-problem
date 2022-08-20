from typing import Callable


def compose(*callables: Callable) -> Callable:
    """
        Returns a new function which is a composition of the given functions.
        The functions are composed in series
        The output result of one function is the input parameter of the next one
        The function on the left is taken as the first function
        There must be at least one function as parameter in order to call compose.

        raise out of index error, object is not callable.
    """
    callables_ = list(callables)
    first_ = callables_.pop(0)

    def composed(*args, **kwargs):
        result = first_(*args, **kwargs)
        for func in callables_:
            result = func(result)
        return result

    return composed
