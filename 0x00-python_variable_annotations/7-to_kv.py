#!/usr/bin/env python3
"""Type-annotated function to_kv"""

def to_kv(k: str, v: int, float) -> list[str, float]:
    """
    Takes a string and an int or float and returns a tuple
    """

    new_float = v ** 2
    return([k, new_float: float]
