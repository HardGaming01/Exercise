# -*- coding: utf-8 -*-
import urllib2
import json
from city import city
cityName = raw_input("你想知道哪个城市的天气：")
cityCode = city.get(cityName)
# 获取天气代码

if cityCode:
    url = "http://www.weather.com.cn/data/cityinfo/%s.html" % cityCode
    content = urllib2.urlopen(url)
else:
    print "没有找到该城市"
# 获取json文件
try:
    data = json.load(content)
    result = data["weatherinfo"]
    temp_str = "%s\n%s ~ %s" % (result["weather"], result["temp1"], result["temp2"])
    print temp_str
except:
    print "查询失败"
