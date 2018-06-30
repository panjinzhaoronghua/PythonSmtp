import requests
import json

yburl = 'https://free-api.heweather.com/s6/weather/forecast'
cyurl = 'https://free-api.heweather.com/s6/weather/lifestyle'
asurl = 'https://free-api.heweather.com/s6/weather/now'
kqurl='https://free-api.heweather.com/s6/air/now'
value = {
    'location':'沈阳',
    'key':'0667fd530b5b42b5974f164d35080784',
    'lang':'zh'
}
ybreq = requests.get(yburl,params=value)#3天的天气
cyreq = requests.get(cyurl,params=value)#生活指数
asreq = requests.get(asurl,params=value)#实时天气
kqreq = requests.get(kqurl,params=value)#空气质量

ybjs = ybreq.json()
cyjs = cyreq.json()
asjs=asreq.json()
kqjs=kqreq.json()#空气质量


print("今日天气：","今日最高温度:",ybjs["HeWeather6"][0]["daily_forecast"][0]["tmp_max"])
print("今日天气：","今日最低温度:",ybjs["HeWeather6"][0]["daily_forecast"][0]["tmp_min"])
print("今日天气：","今日风向:",ybjs["HeWeather6"][0]["daily_forecast"][0]["wind_dir"])
print("今日天气：","今日降水量:",ybjs["HeWeather6"][0]["daily_forecast"][0]["pcpn"])
print("今日天气：","今日紫外线强度指数:",ybjs["HeWeather6"][0]["daily_forecast"][0]["uv_index"])
print("今日天气：","今日日出时间:",ybjs["HeWeather6"][0]["daily_forecast"][0]["sr"])
print("今日天气：","今日日落时间:",ybjs["HeWeather6"][0]["daily_forecast"][0]["ss"])

print("空气质量:","空气质量数据更新时间:",kqjs["HeWeather6"][0]['air_now_station'][2]['pub_time'])
print("空气质量:","空气质量检测地点:",kqjs["HeWeather6"][0]['air_now_station'][2]['air_sta'])
print("空气质量:","空气质量:",kqjs["HeWeather6"][0]['air_now_station'][2]['qlty'])
print("空气质量:","空气质量指数:",kqjs["HeWeather6"][0]['air_now_station'][2]['aqi'])

print("实时天气:","体感温度:",asjs["HeWeather6"][0]["now"]["fl"])
print("实时天气:","温度:",asjs["HeWeather6"][0]["now"]["tmp"])
print("实时天气:","风向:",asjs["HeWeather6"][0]["now"]["wind_dir"])
print("实时天气:","风力:",asjs["HeWeather6"][0]["now"]["wind_sc"])


print("生活指数:","舒适度指数:",cyjs["HeWeather6"][0]["lifestyle"][0]['brf'],cyjs["HeWeather6"][0]["lifestyle"][0]['txt'])
print("生活指数:","穿衣指数:",cyjs["HeWeather6"][0]["lifestyle"][1]['brf'],cyjs["HeWeather6"][0]["lifestyle"][1]['txt'])
print("生活指数:","运动指数:",cyjs["HeWeather6"][0]["lifestyle"][3]['brf'],cyjs["HeWeather6"][0]["lifestyle"][3]['txt'])
