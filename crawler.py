#甚麼是AJAX? 一種JavaScript技術 (在chrome裡面的開發人員中叫XHR)

import urllib.request as req
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=6cd82dbc2a4c18355b683320d4c9012f"
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
})
with req.urlopen(request) as response:
    Data=response.read().decode("utf-8") #根據觀察，取得的資料是json模式

#解析JSON格式資料，取得每篇文章標題
import json
Data=json.loads(Data) #把原始資料解析成字典/列表的表示形式

#取得JSON資料中的文章標題列表
posts=Data["data"]["top_products"]["prod_list"]
for key in posts:
    print(key["name"])