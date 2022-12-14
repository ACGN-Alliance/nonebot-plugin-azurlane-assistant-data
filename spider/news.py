# Python Script Created by MRS
from const import DATA_PATH, DOMIN
from base_func import get_content

from lxml import etree

async def get_latest_news():
    news_page = await get_content("https://wiki.biligame.com/blhx/%E6%96%B0%E9%97%BB%E5%85%AC%E5%91%8A")
    e = etree.HTML(news_page)
    news_url = e.xpath("//div[@class=\"bili-list-order\"]/a/@href")[0]
    detail_page = await get_content(DOMIN + news_url)
    e0 = etree.HTML(detail_page)
    news = e0.xpath("//div[@id=\"mw-content-text\"]//div[@style=\"font-size:15px;line-height: 1.7em;\"]//text()")
    news_str: str = "×数据来源为碧蓝航线wiki,可能和官方通告不同步×\n"
    for i in news:
        news_str += i
    return news_str

if __name__ == '__main__':
    import asyncio
    new = asyncio.run(get_latest_news())
    print(new)