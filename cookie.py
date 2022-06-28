#基本流程:
#   1.連線到特定網址抓取資料。
#   2.解析資料，取得實際想要的部分。
#關鍵心法: 盡可能地讓程式模仿成一個普通的使用者。
#Cookie:網路存放在瀏覽器的一小段內容。
#與伺服器的互動:
#   連線時，放在Request Headers中送出。

#實際練習:
import urllib.request as req
def getData(src):
    #url="https://www.ptt.cc/bbs/Gossiping/index.html" --->如果要抓其他頁的資料，這邊要先刪除不然跑不到別頁去
    request=req.Request(src,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #解析原始碼，取得文章標籤
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")
    for title in titles:
        if title.a !=None:
            print(title.a.string) #如果包含a標籤(沒有被刪除)，印出來
    #抓取上一頁連結
    nextLink=root.find("a",string="‹ 上頁") #用內文對應a標籤
    return nextLink["href"] #這邊的return要注意，有return才會執行
#主程序:抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1

