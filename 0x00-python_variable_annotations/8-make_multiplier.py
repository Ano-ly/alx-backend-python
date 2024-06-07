#!/usr/bin/env python3
"""Make-multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function"""

    def new_multiplier(arg: float):
        """New_multiplier function"""

        return (multiplier * arg)
    return (new_multiplier)
