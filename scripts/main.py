from build_simulator.data_spider import build_data
from ship.data_spider import ship_data

import sys, platform
sys.path.append(".")

async def run():
    # await build_data()
    await ship_data()

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(run())