import asyncio
import random


async def wait_random(max_delay=10):
    # return random value
    value = random.uniform(0, max_delay)
    await asyncio.sleep(0, max_delay)

    return value
