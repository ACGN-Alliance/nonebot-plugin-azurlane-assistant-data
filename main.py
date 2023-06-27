import json
import os
import sys, pathlib
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

from scripts.build_simulator.data_spider import build_data
from scripts.build_simulator.history_pool import get_his_pool
from scripts.ship.data_spider import ship_data
from scripts.equip.spider import get_ori_page

sys.path.append(pathlib.Path.cwd().parent.as_posix())

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(ship_data)
        task2 = executor.submit(build_data)
        task3 = executor.submit(get_his_pool)
        task4 = executor.submit(get_ori_page)

        wait([task1, task2, task3, task4], return_when=ALL_COMPLETED)
    print("=======数据同步完成=======")
    # get_ori_page()