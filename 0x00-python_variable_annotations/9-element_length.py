#!/usr/bin/env python3
"""Ducktyped function"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing the lists in the list
    supplied as argument, and their respective lengths
    """

    return [(i, len(i)) for i in lst]
