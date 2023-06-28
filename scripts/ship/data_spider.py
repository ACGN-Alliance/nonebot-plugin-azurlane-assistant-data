import os, json, re, pathlib

from bs4 import BeautifulSoup

from .ship_model import Ship
from ..utils import get_content


def ship_data():
    print("===开始同步\"舰船资料\"数据===")
    url_prefix = "https://wiki.biligame.com"
    cot = get_content("https://wiki.biligame.com/blhx/%E8%88%B0%E8%88%B9%E5%9B%BE%E9%89%B4")
    soup = BeautifulSoup(cot, "html.parser")

    leng = len(soup.find_all("div", class_="jntj-1 divsort"))
    file_dir = os.path.join(pathlib.Path.cwd().parent, "data/azurlane/ship.json")
    if os.path.exists(file_dir):
        if json.load(open(file_dir, "r", encoding="utf-8"))["total_num"] == leng:
            print("===舰船资料无更新,跳过同步步骤===")
            return
    else:
        pass

    slist = []
    for ship in soup.find_all("div", class_="jntj-1 divsort"):
        alias = []
        for i in ship.find_all("span", class_="jntj-4"):
            pattern = re.compile(r">(?P<raw>.*?)<br/>(?P<now>.*?)<")
            match = re.search(pattern, str(i.contents[-1]))
            if match is None:
                name = i.text
                break
            name = match.group("now")
            alias.append(match.group("raw"))

        iname = ship.find("div", class_="jntj-3").find("img")["alt"]
        if iname.find("决战方案") != -1 or iname.find("海上传奇") != -1:
            rarity = 4
        elif iname.find("超稀有") != -1 or iname.find("最高方案") != -1:
            rarity = 3
        elif iname.find("精锐") != -1:
            rarity = 2
        elif iname.find("稀有") != -1:
            rarity = 1
        elif iname.find("普通") != -1:
            rarity = 0
        else:
            print(f"稀有度出错:{name}\n")
            pass

        wiki_url = ship.find("a")["href"]
        img_url = ship.find("div", class_="jntj-2").find("img")["src"]
        local_url = "data/img/ship_icon/" + name + ".png"

        ship = Ship(
            name=name,
            rarity=rarity,
            wiki_page=url_prefix + wiki_url,
            remote_icon_path=str(img_url),
            local_icon_path=str(local_url),
            alias=alias
        )
        sdata = ship.json(ensure_ascii=False)
        slist.append(json.loads(sdata))

    with open(file_dir, "w", encoding="utf-8") as f:
        json.dump({"total_num": leng, "data": slist}, f, ensure_ascii=False, indent=4)
    print("===舰船资料同步完成===")
