import sys
from concurrent.futures import ThreadPoolExecutor, wait

from build_simulator.data_spider import build_data
from build_simulator.history_pool import get_his_pool
from ship.data_spider import ship_data
from equip.spider import get_ori_page

sys.path.append(".")

if __name__ == '__main__':
    # with ThreadPoolExecutor(max_workers=3) as executor:
        # task1 = executor.submit(ship_data)
        # task2 = executor.submit(build_data)
        # task3 = executor.submit(get_his_pool)
        # wait([task1, task2, task3], return_when="ALL_COMPLETED")
        # print("=======数据同步完成=======")

    get_ori_page()