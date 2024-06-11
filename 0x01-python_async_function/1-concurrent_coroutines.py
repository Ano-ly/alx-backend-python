#!/usr/bin/env python3
"""Contains async routine wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that awaits several spawns of wait_random"""

    i: int = 0
    delays: List[float] = []
    while i < n:
        delays.append(await wait_random(max_delay))
        i += 1
    return (delays)
