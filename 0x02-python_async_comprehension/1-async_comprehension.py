#!/usr/bin/env python3
"""Contains async comprehension function"""
from typing import List


async def async_comprehension() -> List[float]:
    """Async comprehension function"""

    return ([i async for i in async_generator()])
