from bs4 import BeautifulSoup
import sys, os, re
# sys.path.append("E:/Code/Github/nonebot-plugin-azurlane-assistant-data")
sys.path.append(os.curdir)

from scripts.build_simulator.init_pool import init_pool
from scripts.utils import get_content

async def build_data():
    print("===开始同步\"建造模拟器\"数据===")

    init_data = init_pool
    cot = await get_content("https://wiki.biligame.com/blhx/%E5%BB%BA%E9%80%A0%E6%A8%A1%E6%8B%9F%E5%99%A8")
    soup = BeautifulSoup(cot, "html.parser")

    init_data["qx"]["ssr"] = [i.text for i in soup.find(id="LightShipBuildingListSuperRare").find_all("span", class_="AF")]
    init_data["qx"]["sr"] = [i.text for i in soup.find(id="LightShipBuildingListElite").find_all("span", class_="AF")]
    init_data["qx"]["r"] = [i.text for i in soup.find(id="LightShipBuildingListRare").find_all("span", class_="AF")]
    init_data["qx"]["n"] = [i.text for i in soup.find(id="LightShipBuildingListNormal").find_all("span", class_="AF")]
    
    init_data["zx"]["ssr"] = [i.text for i in soup.find(id="HeavyShipBuildingListSuperRare").find_all("span", class_="AF")]
    init_data["zx"]["sr"] = [i.text for i in soup.find(id="HeavyShipBuildingListElite").find_all("span", class_="AF")]
    init_data["zx"]["r"] = [i.text for i in soup.find(id="HeavyShipBuildingListRare").find_all("span", class_="AF")]
    init_data["zx"]["n"] = [i.text for i in soup.find(id="HeavyShipBuildingListNormal").find_all("span", class_="AF")]
    
    init_data["tx"]["ssr"] = [i.text for i in soup.find(id="AircraftShipBuildingListSuperRare").find_all("span", class_="AF")]
    init_data["tx"]["sr"] = [i.text for i in soup.find(id="AircraftShipBuildingListElite").find_all("span", class_="AF")]
    init_data["tx"]["r"] = [i.text for i in soup.find(id="AircraftShipBuildingListRare").find_all("span", class_="AF")]
    init_data["tx"]["n"] = [i.text for i in soup.find(id="AircraftShipBuildingListNormal").find_all("span", class_="AF")]

    cot1 = await get_content("https://wiki.biligame.com/blhx/%E5%BB%BA%E9%80%A0%E6%A8%A1%E6%8B%9F%E5%99%A8/%E9%99%90%E6%97%B6%E5%BB%BA%E9%80%A0")
    soup1 = BeautifulSoup(cot1, "html.parser")
    temp_lst = []
    for i in soup1.find_all("tr", class_="speciallist"):
        j = i.find("span", class_="nowrap")["style"]
        if(j == "color:#ee494c"):
            j = "ur"
        elif(j == "color:#c90"):
            j = "ssr"
        elif(j == "color:#8000ff"):
            j = "sr"
        else:
            j = "r"
        
        rate = float(i.find("span", class_="TimeLimitBuildingSpacalPR").text)
        name = i.find("span", class_="AF").text
        temp_lst.append({"name": name, "rarity": j, "rate": rate})
    for i in temp_lst:
        init_data["xd"].append(i)

    soup2 = BeautifulSoup(cot, "html.parser")
    rate = [int(re.findall(r"(\d.*)%$", i.text)[0])/100 for i in soup2.find_all("th", style=re.compile("background-color:#")) if (not "艘" in i.text)]

    init_data["data"]["qx"]["ssr"] = rate[0]
    init_data["data"]["qx"]["sr"] = rate[1]
    init_data["data"]["qx"]["r"] = rate[2]
    init_data["data"]["qx"]["n"] = rate[3]
    init_data["data"]["zx"]["ssr"] = rate[4]
    init_data["data"]["zx"]["sr"] = rate[5]
    init_data["data"]["zx"]["r"] = rate[6]
    init_data["data"]["zx"]["n"] = rate[7]
    init_data["data"]["tx"]["ssr"] = rate[8]
    init_data["data"]["tx"]["sr"] = rate[9]
    init_data["data"]["tx"]["r"] = rate[10]
    init_data["data"]["tx"]["n"] = rate[11]

    import pathlib, json
    with open(pathlib.Path.cwd()+"/azurlane/pool.json", "w", encoding="utf-8") as f:
        json.dump(init_data, f, ensure_ascii=False, indent=4)

    # return init_data