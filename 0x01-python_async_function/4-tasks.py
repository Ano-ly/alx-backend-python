#!/usr/bin/env python3
"""Contains async routine wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that awaits several coroutines"""

    delays: List[float] = []
    tasks = []
    for i in range(0, n):
        task = task_wait_random(max_delay))
        tasks.append(task)
    for item in asyncio.as_completed(tasks):
        delays.append(await item)
    return (delays)
