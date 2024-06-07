#!/usr/bin/env python3
"""Type-annotated function to_kv"""

def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """
    Takes a string and an int or float and returns a tuple
    """

    return((k, v ** 2))
