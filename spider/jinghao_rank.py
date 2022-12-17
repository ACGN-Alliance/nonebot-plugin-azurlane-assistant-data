# Python Script Created by MRS
import asyncio, json, hashlib
from lxml import etree

from base_func import get_content
from const import DATA_PATH, IMG_PATH

img_path = IMG_PATH + "jinghao_rank/"
rank_lst = ["认知觉醒主线推荐榜.jpg", "认知觉醒大世界推荐榜.jpg", "装备一图榜.jpg", "萌新入坑舰船推荐榜.png", "萌新入坑装备推荐榜.png", "兵装推荐榜.jpg", "专武推荐榜.png", "兑换装备推荐榜.png", "装备研发推荐榜.png", "改造舰船推荐榜.png", "跨队舰船推荐榜.png", "氪金榜.png"]

async def download_jinghao_rank():
    print("***开始同步井号榜数据***")
    cot = await get_content("https://wiki.biligame.com/blhx/%E4%BA%95%E5%8F%B7%E7%A2%A7%E8%93%9D%E6%A6%9C%E5%90%88%E9%9B%86")
    e = etree.HTML(cot)
    with open(DATA_PATH + "jinghao_rank.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    count = 0
    for i in rank_lst:
        count += 1
        xpath_path = "//*[@id=\"mw-content-text\"]//img[@alt=\"" + i + "\"]/@src"
        img: bytes = await get_content(e.xpath(xpath_path)[0])
        with open(img_path + i, "wb") as f0:
            f0.write(img)
        data[("img" + str(count))] = {
            "name": i,
            "hash": hashlib.md5(img).hexdigest()
        }
        print( i + "    同步完毕")
    with open(DATA_PATH + "jinghao_rank.json", "w", encoding="utf-8") as f0:
        json.dump(data, f0, ensure_ascii=False, indent=4)

    print("***井号榜数据同步完毕***")

if __name__ == '__main__':
    asyncio.run(download_jinghao_rank())