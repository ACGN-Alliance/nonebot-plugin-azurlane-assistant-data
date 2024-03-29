# Azurlane-data
## 此仓库代码正在准备重构
本仓库原为nonebot-plugin-azurlane-assistant(仓库已归档)的数据仓库，用以存储使用Github Actions自动爬取碧蓝航线wiki的数据  
这里的数据可以随意使用  

<b>欢迎各位进行[Pr](https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/pulls)帮助更新数据源</b>

本仓库已建立Gitee镜像仓库供国内进行快速访问 [Gitee](https://gitee.com/mrslouzk/nonebot-plugin-azurlane-assistant-data)

# 数据内容
- [建造池数据](https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/blob/main/data/pool.json)
- [舰船数据]()
- [装备数据]()
- 重樱/铁血船名对照(准备重构)
- 井号榜图片(准备重构)

......剩余的努力制作中

# 更新计划
- ~~舰船数据爬取~~
- 提供标准调用函数
- ~~添加Gitee镜像仓库~~
- 代码大幅优化与重构
- 部署成api方便调用(可能不会做)
- 详情请见[todo](./todo.md)

# 如何进行Pull Request
- fork本仓库
- 向scripts文件夹当中添加爬虫脚本(网页请求函数请尽量用utils.py里的get_content, 网页解析推荐bs4)
- 将函数加入scripts/main.py当中
- 提交pr并等待审核

# 使用本数据的仓库
> 可作为接口样例参考
- [Azurlane-helper-bot](https://github.com/MRSlouzk/Azurlane-helper-bot)(活跃)
- [nonebot-plugin-azurlane-assistant](https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant)(已归档)

# 鸣谢
- [碧蓝航线wiki](https://wiki.biligame.com/blhx/%E9%A6%96%E9%A1%B5)
- [bawiki-data](https://github.com/lgc2333/bawiki-data)

PS：如果有碧蓝海事局的大佬看到本仓库可以联系我

# 如何联系我
- 邮箱: mrslouzk@qq.com
- QQ群: 757739422
