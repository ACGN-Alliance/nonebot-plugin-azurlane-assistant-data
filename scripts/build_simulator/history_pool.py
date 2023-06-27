from bs4 import BeautifulSoup

from scripts.utils import get_content

def get_his_pool():
    his_data = {}

    print("===开始同步\"历史建造池\"数据===")
    url = "https://wiki.biligame.com/blhx/%E5%BB%BA%E9%80%A0%E6%A8%A1%E6%8B%9F%E5%99%A8/%E9%99%90%E6%97%B6%E5%BB%BA" \
          "%E9%80%A0"
    cot = get_content(url)
    soup = BeautifulSoup(cot, "html.parser")

    par = soup.find("div", style="border:2px solid #cecece;border-radius:5px;height:400px;overflow:auto")

    temp_date = ""
    for ele in par:
        if("h3" in str(ele)):
            sp = BeautifulSoup(str(ele), "html.parser")
            date = sp.find("span").get("id")
            if(date is not None):
                if("E" in date):
                    continue
            temp_date = date
            his_data[date] = []
        elif("ul" in str(ele)):
            sp = BeautifulSoup(str(ele), "html.parser")
            name = sp.find("span", class_="AF").text
            rarity = float(sp.find("sup").find("b").text.replace("%", ""))/100
            his_data[temp_date].append({
                "name": name,
                "rarity": rarity
            })
        else:
            pass

    import pathlib, json
    with open(f"{str(pathlib.Path.cwd().parent)}/data/azurlane/his_pool.json", "w", encoding="utf-8") as f:
        json.dump(his_data, f, ensure_ascii=False, indent=4)

    print("===历史建造池同步完成===")