import os, json
import pathlib
import time
from typing import Tuple
from urllib.parse import unquote

from scripts.utils import get_content
from .model import ShipEquip

from bs4 import BeautifulSoup, NavigableString, Tag

def attrs_parse(data: NavigableString) -> dict:
    att_lst = data.find_all("li", recursive=False)
    res_dict = {}

    parent_ele = ""
    extra_text = ""
    for i, ele in enumerate(att_lst):
        if ele.get("style"):
            continue
        elif(i == len(att_lst) - 1):
            break

        if not ele.find_all("ul", class_="equip", recursive=False):
            key = ele.find("th").text
            res_dict[key] = {}
            # 判断是否为单行属性
            if not att_lst[i+1].find_all("ul", class_="equip", recursive=False):
                res_dict[key] = ele.find("td").text
                continue

            parent_ele = key
            if ele.find("td"):
                extra_text = ele.find("td").text
        else:
            if extra_text:
                res_dict[parent_ele]["备注"] = extra_text
                extra_text = ""

            chd_lst = ele.find("ul").find_all("li", recursive=False)
            temp_key = ""
            for j, ele_1 in enumerate(chd_lst):
                if not ele_1:
                    break

                # 二层嵌套
                if ele_1.find_all("ul"):
                    che_lst = ele_1.find("ul").find_all("li", recursive=False)
                    if che_lst:
                        temp_key_2 = ""
                        for k, ele_2 in enumerate(che_lst):
                            if not ele_2:
                                break

                            if ele_2.find_all("li"):
                                for ele_3 in ele_2.find_all("li"):
                                    if not ele_3:
                                        break
                                    key_2 = ele_3.find("th").text
                                    res_dict[parent_ele][temp_key][temp_key_2][key_2] = ele_3.find("td").text
                                continue

                            key_1 = ele_2.find("th").text
                            # res_dict[parent_ele][temp_key][key_1] = ele_2.find("td").text
                            try:
                                if che_lst[k+1].find("li"):
                                    temp_key_2 = key_1
                                    res_dict[parent_ele][temp_key][key_1] = {}
                                else:
                                    res_dict[parent_ele][temp_key][key_1] = ele_2.find("td").text
                            except IndexError:
                                res_dict[parent_ele][temp_key][key_1] = ele_2.find("td").text
                        continue

                key = ele_1.find("th").text
                try:
                    if chd_lst[j+1].find("li"):
                        temp_key = key
                        res_dict[parent_ele][key] = {}
                    else:
                        res_dict[parent_ele][key] = ele_1.find("td").text
                except IndexError:
                    res_dict[parent_ele][key] = ele_1.find("td").text

    return res_dict

def parse_page_data(url: str) -> dict:
    page = get_content(url)
    soup = BeautifulSoup(page, "html.parser")

    name = str(soup.find("ul", class_="equip").find("b").find("a").text)
    color = soup.find("ul", class_="equip").find_all("li")[0].get("style")
    if(color == "text-align:center;font-size:1.2em;background:linear-gradient(135deg,#59AE6A,#48AE96,#60D9EC,#65A5D5,#9491E0,#C382A4)"):
        rarity = 4
    elif(color == "text-align:center;font-size:1.2em;background:#f9f593"):
        rarity = 3
    elif(color == "text-align:center;font-size:1.2em;background:#ae90ef"):
        rarity = 2
    elif(color == "text-align:center;font-size:1.2em;background:#1bb7eb"):
        rarity = 1
    elif(color == "text-align:center;font-size:1.2em;background:#dbdcdf"):
        rarity = 0
    else:
        raise Exception("稀有度出错" + name)
    level = str(soup.find("td", style="width:25%;vertical-align:top;font-size:2em").find("b").text)
    type_ = soup.find("div", style="width:100%;border:2px red solid;border-radius:2px;font-size:0.8em")
    if type_ is not None:
        type_ = str(type_.text)
    else:
        type_ = "特殊兵装"

    attrs = attrs_parse(soup.find("ul", class_="equip"))

    suit_type = soup.find("ul", class_="equip").find_all("li")[-1].find("table").get("data-适用舰种")
    suit_type_lst = suit_type.split(",")
    suit_type_lst = [i for i in suit_type_lst if i]
    name_lst = name.split("/")
    if len(name_lst) == 1:
        eq = ShipEquip(
            name=name_lst[0],
            rarity=rarity,
            level=level,
            type=type_,
            attrs=attrs,
            suit_type=suit_type_lst
        )
    else:
        eq = ShipEquip(
            name=name_lst[0],
            alias=name_lst[1:],
            rarity=rarity,
            level=level,
            type=type_,
            attrs=attrs,
            suit_type=suit_type_lst
        )

    return eq.dict()

def get_ori_page():
    prefix_url = "https://wiki.biligame.com"
    update_lst = []

    page = get_content("https://wiki.biligame.com/blhx/%E8%A3%85%E5%A4%87%E5%9B%BE%E9%89%B4")
    soup = BeautifulSoup(page, "html.parser")

    # 检查是否有更新
    file_list = os.listdir(f"{pathlib.Path.cwd().parent}/azurlane/equip")
    new_file_lst = []
    for file in file_list:
        nfile = file[0:-5]
        nfile = nfile.replace("\\", "/")
        new_file_lst.append(nfile)
    if(len(file_list) == len(soup.find_all("div", class_="divsort jntj-1"))):
        print("===装备资料无更新,跳过同步步骤===")
        return

    # 获取更新列表
    for ele in soup.find_all("div", class_="divsort jntj-1"):
        url = ele.find("a")["href"]
        name = ele.find_all("a")[1].text
        if(name in new_file_lst):
            continue
        update_lst.append((name, prefix_url + url))

    print("共需要下载" + str(len(update_lst)) + "个装备资料\n")
    for i, url in enumerate(update_lst):
        print("正在下载" + unquote(url[1].split("/")[-1][0:-3]) + f"的资料, 第{i+1}个")
        data = parse_page_data(url[1])
        file_name = url[0].replace("/", "\\")
        with open(f"{pathlib.Path.cwd().parent}/azurlane/equip/{file_name}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
        time.sleep(1.5)