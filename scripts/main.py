from build_simulator.data_spider import build_data

import sys
sys.path.append(".")

async def run():
    await build_data()

if __name__ == "__main__":
    import asyncio, json
    loop = asyncio.get_event_loop()
    data = (loop.run_until_complete(build_data()))