# Python Script Created by MRS
import asyncio

from build_simulator import simulate_data_spider
from jinghao_rank import download_jinghao_rank
from ship_icon import ship_icon_download

async def run():
    print("*****资源同步开始*****")
    await simulate_data_spider()  # 大建池数据
    await download_jinghao_rank()  # 井号榜同步
    await ship_icon_download()  #舰船图标下载
    print("*****资源同步完成*****")

if __name__ == '__main__':
    asyncio.run(run())