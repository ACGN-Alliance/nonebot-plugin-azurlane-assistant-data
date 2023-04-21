from pydantic import BaseModel, Field, HttpUrl
from typing import Tuple, Optional, Union, Dict, List
from PIL import Image, ImageDraw, ImageFont

class ShipEquip(BaseModel):
    name: str
    alias: List[str] = Field(default_factory=list)
    rarity: int  # 0~4: 白，蓝，紫，金，彩
    level: str  # T0~T4
    type: str
    # 驱逐炮，轻巡炮，重巡炮，大口径重巡炮，战列炮，絮库夫炮，水面鱼雷，潜艇鱼雷，防空炮，导弹，战斗机，轰炸机，鱼雷机，水上机，反潜机，设备，特殊兵装

    attrs: dict = Field(default_factory=dict)
    suit_type: List[str]  # 驱逐，轻巡，重巡，超巡，战巡，战列，轻航，航母，航战，潜母，重炮，潜艇，维修，运输，风帆

    img_url: HttpUrl = Field(default_factory=str)

    def load_dict(self, data: dict):
        self.name = data['name']
        self.rarity = data['rarity']
        self.level = data['level']
        self.type = data['type']
        self.attrs = data['attrs']
        self.suit_type = data['suit_type']
        self.img_url = data['img_url']

    def to_pic(self, f) -> bytes:
        img = Image.new("RGBA", (576, 1000), (0, 0, 0, 120))
        draw = ImageDraw.Draw(img)
        draw.rectangle(xy=(0, 0, 576, 60), fill=(0, 0, 0, 180))

        # return img.tobytes()
        return img.save(f, format='JPEG')