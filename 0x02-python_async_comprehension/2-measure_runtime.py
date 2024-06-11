#!/usr/bin/env python3
"""Contains function to measure time for an async operation"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Function that measures time it takes for four
    parallel async_conprehensions
    """

    time_one: float = time.perf_counter()
    result = asyncio.gather(async_comprehension(),
                            async_comprehension(),
                            async_comprehension(),
                            async_comprehension())
    await result
    time_two = time.perf_counter()
    return (time_two - time_one)
