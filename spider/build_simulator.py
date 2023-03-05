# Python Script Created by MRS
from typing import List

from lxml import etree
import json

from const import DATA_PATH
from base_func import get_content, check_path

init_pool = {
    "qx": {
        "ssr": [],
        "sr": [],
        "r": [],
        "n": []
    },
    "zx": {
        "ssr": [],
        "sr": [],
        "r": [],
        "n": []
    },
    "tx": {
        "ssr": [],
        "sr": [],
        "r": [],
        "n": []
    },
    "xd": [],
    "data": {
        "qx": {
            "ssr": 0,
            "sr": 0,
            "r": 0,
            "n": 0
        },
        "zx": {
            "ssr": 0,
            "sr": 0,
            "r": 0,
            "n": 0
        },
        "tx": {
            "ssr": 0,
            "sr": 0,
            "r": 0,
            "n": 0
        },
        "xd": {
            "ssr": 0,
            "sr": 0,
            "r": 0,
            "n": 0
        }
    }
}

async def simulate_data_spider():
    print("***开始同步\"建造模拟器\"数据***")
    xd_ssr_rate = 0.07
    xd_sr_rate = 0.12
    xd_r_rate = 0.51
    xd_n_rate = 0.3 # 限定池的其他船原始概率数据

    await check_path(DATA_PATH)
    data = init_pool
    cot = await get_content("https://wiki.biligame.com/blhx/%E5%BB%BA%E9%80%A0%E6%A8%A1%E6%8B%9F%E5%99%A8")
    e = etree.HTML(cot)
    for i in e.xpath("//td[@id=\"LightShipBuildingListSuperRare\"]//span/@title"):
        data["qx"]["ssr"].append(i)
    for i in e.xpath("//td[@id=\"LightShipBuildingListElite\"]//span/@title"):
        data["qx"]["sr"].append(i)
    for i in e.xpath("//td[@id=\"LightShipBuildingListRare\"]//span/@title"):
        data["qx"]["r"].append(i)
    for i in e.xpath("//td[@id=\"LightShipBuildingListNormal\"]//span/@title"):
        data["qx"]["n"].append(i)

    for i in e.xpath("//td[@id=\"HeavyShipBuildingListSuperRare\"]//span/@title"):
        data["zx"]["ssr"].append(i)
    for i in e.xpath("//td[@id=\"HeavyShipBuildingListElite\"]//span/@title"):
        data["zx"]["sr"].append(i)
    for i in e.xpath("//td[@id=\"HeavyShipBuildingListRare\"]//span/@title"):
        data["zx"]["r"].append(i)
    for i in e.xpath("//td[@id=\"HeavyShipBuildingListNormal\"]//span/@title"):
        data["zx"]["n"].append(i)

    for i in e.xpath("//td[@id=\"AircraftShipBuildingListSuperRare\"]//span/@title"):
        data["tx"]["ssr"].append(i)
    for i in e.xpath("//td[@id=\"AircraftShipBuildingListElite\"]//span/@title"):
        data["tx"]["sr"].append(i)
    for i in e.xpath("//td[@id=\"AircraftShipBuildingListRare\"]//span/@title"):
        data["tx"]["r"].append(i)
    for i in e.xpath("//td[@id=\"AircraftShipBuildingListNormal\"]//span/@title"):
        data["tx"]["n"].append(i)

    ######## 限定 ########
    data["data"]["xd"]["ssr"] = 0.07
    data["data"]["xd"]["sr"] = 0.12
    data["data"]["xd"]["r"] = 0.51
    data["data"]["xd"]["n"] = 0.3

    cot0 = await get_content("https://wiki.biligame.com/blhx/%E5%BB%BA%E9%80%A0%E6%A8%A1%E6%8B%9F%E5%99%A8/%E9%99%90%E6%97%B6%E5%BB%BA%E9%80%A0")
    e0 = etree.HTML(cot0)
    temp_lst: List[dict] = []
    for j in e0.xpath("//tr[@class=\"speciallist\"]//span[@class=\"nowrap\"]/@style"):
        if(j == "color:#ee494c"):
            j = "ur"
        elif(j == "color:#c90"):
            j = "ssr"
        elif(j == "color:#8000ff"):
            j = "sr"
        else:
            j = "r"
        temp_lst.append({"name": "", "rarity": j, "rate": 0})
    ship_info = e0.xpath("//tr[@class=\"speciallist\"]//span/text()")
    for i in range(len(temp_lst) * 2):
        if(i % 2 != 0):
            continue
        temp_lst[int(int(i) / 2)]["name"] = ship_info[i+1]
        temp_lst[int(int(i) / 2)]["rate"] = float(ship_info[i]) / 100
        rar = temp_lst[int(int(i) / 2)]["rarity"]
        if(rar == "ur"): continue
        data["data"]["xd"][rar] -= float(ship_info[i]) / 100 # 限定池的概率数据扣除限定UP的数据

    for i in temp_lst:
        data["xd"].append(i)
    ####################

    rate = e.xpath("//div[@class=\"LotusRoot\"]//tr[1]/th/text()")
    rate_num: list = []
    for i in rate:
        i: str
        i = i.replace("%\n", "")
        i = i.split()[1]
        rate_num.append(int(i)/100)

    data["data"]["qx"]["ssr"] = rate_num[0]
    data["data"]["qx"]["sr"] = rate_num[1]
    data["data"]["qx"]["r"] = rate_num[2]
    data["data"]["qx"]["n"] = rate_num[3]
    data["data"]["zx"]["ssr"] = rate_num[4]
    data["data"]["zx"]["sr"] = rate_num[5]
    data["data"]["zx"]["r"] = rate_num[6]
    data["data"]["zx"]["n"] = rate_num[7]
    data["data"]["tx"]["ssr"] = rate_num[8]
    data["data"]["tx"]["sr"] = rate_num[9]
    data["data"]["tx"]["r"] = rate_num[10]
    data["data"]["tx"]["n"] = rate_num[11]

    with open(DATA_PATH + "pool.json", "w", encoding="utf-8") as f2:
        json.dump(data, f2, ensure_ascii=False, indent=4)

    print("***建造池数据同步完成***")

if __name__ == '__main__':
    import asyncio
    asyncio.run(simulate_data_spider())