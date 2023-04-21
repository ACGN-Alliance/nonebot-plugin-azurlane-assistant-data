from json import load, loads
from scripts.equip.model import ShipEquip

def load_and_parse():
    data = load(open('example.json', 'r', encoding='utf-8'))
    se = ShipEquip(data)
    with open("new.jpg", "wb") as f:
        se.to_pic(f)
    return data


if __name__ == '__main__':
    print(load_and_parse())
