#!/usr/bin/env python3
"""Ducktyped function"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any,  None]:
    """Return the firat element of a sequence safely"""

    if lst:
        return lst[0]
    else:
        return None
