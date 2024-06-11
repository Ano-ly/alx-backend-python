#!/usr/bin/env python3
"""Async function to wait for random number of seconds"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Async function that waits for random seconds"""

    sleep_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return (sleep_time)
