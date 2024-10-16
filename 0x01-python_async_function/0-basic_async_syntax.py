#!/usr/bin/env python3
""" Takes int arg, waits for random delay """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Wait for random delay between 0 and max_delay, returns that """
    actual_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
