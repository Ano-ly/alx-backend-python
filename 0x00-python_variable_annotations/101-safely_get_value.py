#!/usr/bin/env python3
"""Type-aannotated"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Function to safely get value of a dictionary"""

    if key in dct:
        return dct[key]
    else:
        return default
