# Python Script Created by MRS
from httpx import AsyncClient, Response
from const import HEADERS
from typing import List

async def check_path(path: str | List[str]):
    """
    检查路径是否存在，不存在则创建

    :param path:路径
    """
    import os
    if(type(path) == str):
        if not os.path.exists(path):
            os.makedirs(path)
    elif(type(path) == list):
        for p in path:
            if not os.path.exists(p):
                os.makedirs(p)
    else:
        raise TypeError("path type error")

async def parse(resp: Response) -> dict | str | bytes:
    header = resp.headers.get("content-type")
    if("html" in header):
        resp.encoding="utf-8"
        return resp.text
    elif("json" in header):
        resp.encoding="utf-8"
        return resp.json()
    elif ("image" in header):
        return resp.content
    else:
        resp.encoding="utf-8"
        return resp.text

async def get_content(
        url: str,
        *args,
        timeout: int = 10,
        **kwargs
) -> dict | str | bytes:
    """
    获取页面

    :param url:链接
    :param timeout:超时时间
    :return:页面响应
    """
    async with AsyncClient(headers=HEADERS, timeout=timeout) as c:
        c: AsyncClient
        resp = await c.get(url=url)
    return (await parse(resp))

#For test
if __name__ == '__main__':
    import asyncio
    asyncio.run(get_content(""))