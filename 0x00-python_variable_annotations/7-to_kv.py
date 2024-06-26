#!/usr/bin/env python3
"""Type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float and returns a tuple
    """

    return ((k, v ** 2))
