# Python Script Created by MRS
from base_func import get_content
from lxml import etree
import json, asyncio

async def simulate_data_spider():
    with open("../data/pool.json", "r", encoding="utf-8") as f:
        data: dict = json.load(f)
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

    rate = e.xpath("//div[@class=\"LotusRoot\"]//tr[1]/th/text()")
    rate_num: [float] = []
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

    with open("../data/pool.json", "w", encoding="utf-8") as f2:
        json.dump(data, f2, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    asyncio.run(main())