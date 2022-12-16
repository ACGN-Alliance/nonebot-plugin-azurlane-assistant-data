# Python Script Created by MRS
from build_simulator import simulate_data_spider
from jinghao_rank import download_jinghao_rank
from ship_icon import ship_icon_download

def run():
    simulate_data_spider()
    download_jinghao_rank()
    ship_icon_download()