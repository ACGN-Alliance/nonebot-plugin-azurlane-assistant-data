import sys
from concurrent.futures import ThreadPoolExecutor, wait

from build_simulator.data_spider import build_data
from build_simulator.history_pool import get_his_pool
from ship.data_spider import ship_data

sys.path.append(".")

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as executor:
        # task1 = executor.submit(ship_data)
        # task2 = executor.submit(build_data)
        task3 = executor.submit(get_his_pool)
        print(task3.result())
        # wait([task1, task2, task3], return_when="ALL_COMPLETED")
        # wait([task3], return_when="ALL_COMPLETED")
        print("=======数据同步完成=======")