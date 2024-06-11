#!/usr/bin/env python3
"""Contains async routine wait_n"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio task"""

    return (asyncio.create_task(wait_random(max_delay)))
