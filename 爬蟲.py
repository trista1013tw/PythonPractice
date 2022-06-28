#基本流程:
#1.連線到特定網址，抓取資料(注意:我們要包裝自己像是正常的使用者:Agent-Headers)。
#2.解析資料，取得實際想要的部分。

#抓取資料(關鍵):盡可能讓程式模仿一個普通使用者的樣子。
#皆喜資料
#1.json格式:可以使用import(python有內建輔助)
#2.HTML格式:資料使用第三方套件BeautifulSoup解析
#   因為下載python時會同時下載PIP套件管理工具，我們可以利用PIP安裝BeautifulSoup，只需下指令:pip install baeutifulsoup4


#實際練習
#抓取ptt打工版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/part-time/index.html"
#建立一個Request物件，附加Request Headers的資訊(讓我們爬蟲看起來像普通人逛網頁)
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

#解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
print(root.title.string) #string-->只抓標籤內的文字
titles=root.find("div",class_="title") #尋找class="title"的div標籤
#.find(要找的標籤名稱,篩選的名稱)
print(titles)
print(titles.a.string)
titless=root.find_all("div",class_="title")
print(titless)
for title in titless:
    if title.a !=None: #如果標籤包含a標籤(沒有被刪除)，印出來
        print(title.a.string)