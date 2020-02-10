# coding=utf-8
from web.testyi import Web



# 打开浏览器
web = Web()
web.baidu()
# 获取疫情信息
text = web.getyiqing()
print(text)

