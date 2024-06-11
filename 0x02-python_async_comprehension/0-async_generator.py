#!/usr/bin/env python3
"""Function for Async comprehensions"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Function that generates random numbers"""

    for i in range(10):
        await asyncio.sleep(1)
        no = random.uniform(0, 10)
        yield no
