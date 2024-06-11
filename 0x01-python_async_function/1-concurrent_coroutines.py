#!/usr/bin/env python3
"""Contains async routine wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that awaits several coroutines"""

    delays: List[float] = []
    tasks = []
    for i in range(0, n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for item in asyncio.as_completed(tasks):
        delays.append(await item)
    return (delays)
