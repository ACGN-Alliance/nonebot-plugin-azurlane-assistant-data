# Python Script Created by MRS
import json
import os

from lxml import etree

from base_func import get_content
from const import DATA_PATH, ROOT_PATH

async def download_japan_ship_contrast():
    print("***开始同步重樱船名对照数据***")
    with open(DATA_PATH + "japan_ship_name.json", "r", encoding="utf-8") as f:
        local_data: dict = json.load(f)
    cot = await get_content("https://wiki.biligame.com/blhx/%E9%87%8D%E6%A8%B1%E8%88%B9%E5%90%8D%E7%A7%B0%E5%AF%B9%E7%85%A7%E8%A1%A8")
    e = etree.HTML(cot)
    if(len(e.xpath("//tr[@class=\"Flour\"]//rb/span")) == len(local_data.keys())):
        print("重樱船名对照数据未更新,跳过同步")
        return
    else:
        for name in e.xpath("//tr[@class=\"Flour\"]//rb/span/text()"):
            if(local_data.get(name) is None):
                info = e.xpath(f"//tr[@class=\"Flour\"]//span[text()=\"{name}\"]/../../../..//span/text()")
                local_data[name] = {
                    "ori": info[2],
                    "pinyin": info[1]
                }
        with open(DATA_PATH + "japan_ship_name.json", "w", encoding="utf-8") as f:
            json.dump(local_data, f, ensure_ascii=False, indent=4)

        print("***重樱船名对照数据同步完成***")

if __name__ == '__main__':
    import asyncio
    asyncio.run(download_japan_ship_contrast())