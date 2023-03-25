from pydantic import BaseModel, Field
from typing import List, Optional

class ShipAttrs(BaseModel):
    durability: int                 # 耐久
    cannon: Optional[int]           # 炮击
    antiaircraft: int               # 防空
    antisubmarine: Optional[int]    # 对潜
    luck: int                       # 幸运
    speed: int                      # 速度
    armor: int                      # 装甲
    thunder: Optional[int]          # 雷击
    aviation: Optional[int]         # 航空
    cost: int                       # 花费
    stuffing: int                   # 装填
    expedient: int                  # 机动
    hit: int                        # 命中

class Ship(BaseModel):
    """
    舰船资料

    Attributes:
        name: 船名  
        rarity: 稀有度(0: N, 1: R, 2: SR, 3: SSR, 4: UR)  
        alias: 别名  
        wiki_page: bwiki页面  
        remote_icon_path: 远程图标路径  
        local_icon_path: 本地图标路径  
        attrs: 属性  
    """
    name: str               # 船名
    rarity: int             # 稀有度(0: N, 1: R, 2: SR, 3: SSR, 4: UR)
    alias: Optional[List[str]]        # 别名
    wiki_page: str = Field(None, description="bwiki页面")
    remote_icon_path: str = Field(None, description="远程图标路径")
    local_icon_path: str = Field(None, description="本地图标路径")
    #attrs: ShipAttrs        # TODO 属性
