# Python Script Created by MRS
import asyncio

from lxml import etree
from base_func import get_content

async def main():
    cot = await get_content("https://wiki.biligame.com/blhx/%E4%BA%95%E5%8F%B7%E7%A2%A7%E8%93%9D%E6%A6%9C%E5%90%88%E9%9B%86")
    e = etree.HTML(cot)
    img_url = e.xpath("//*[@id=\"mw-content-text\"]//img[@alt=\"认知觉醒主线推荐榜.jpg\"]/@src")[0]
    img = await get_content(img_url)
    return img

if __name__ == '__main__':
    ig = asyncio.run(main())
    with open("../data/1.jpg", "wb") as f:
        f.write(ig)
#TODO 解决出现大量wiki数据导致的网络崩溃|方案：建立第三方数据库(github)