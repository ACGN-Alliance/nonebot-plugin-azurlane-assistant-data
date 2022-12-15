# Python Script Created by MRS
import asyncio, os, logging, re
from lxml import etree

from base_func import get_content

IMG_PATH = "../img/ship_icon/"

def resource_check(
        page: str
    ) -> bool:
    e = etree.HTML(page)
    num = len(e.xpath("//div[@class=\"jntj-2\"]/div[1]//img/@src"))
    if (len(os.listdir(IMG_PATH)) != num):
        return False
    else:
        return True

async def ship_icon_download():
    print("开始检查图标资源")
    cot = await get_content("https://wiki.biligame.com/blhx/%E8%88%B0%E8%88%B9%E5%9B%BE%E9%89%B4")
    if(resource_check(cot)):
        return
    else:
        e = etree.HTML(cot)
        local_file_lst = os.listdir(IMG_PATH)
        file_to_download = []
        for i in local_file_lst:
            local_file_lst[local_file_lst.index(i)] = i.split(".")[0] #去除文件后缀名
        for i in e.xpath("//span[@class=\"jntj-4\"]//a/text()"):
            if (i == "赤城(μ兵装)(凰(μ兵装))"):
                i = "赤城(μ兵装)"
            elif(i == "大凤(μ兵装)(鹩(μ兵装))"):
                i = "大凤(μ兵装)"
            if("μ兵装" not in i):
                i = re.sub(r"(\(.*\))", "", i)
            i = i.replace(".", "")
            if (i in local_file_lst):
                continue
            else:
                file_to_download.append(i)
        if(len(file_to_download) == 0):
            print("图标资源齐全,无须额外下载")
            return
        else:
            print("需要下载的图标资源有: " + str(file_to_download))
            for i in file_to_download:
                xpth_url = "//img[@alt=\"" + i + "头像.jpg\"]/@src"
                img_url = e.xpath(xpth_url)[0]
                img = await get_content(img_url)
                with open(IMG_PATH + i + ".png", "wb") as f:
                    f.write(img)
            print("图标资源下载完成")

if __name__ == '__main__':
    asyncio.run(ship_icon_download())