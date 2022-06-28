#網路連線、公開資料串接
#網路連線
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    #data=response.read().decode("utf-8")#如果有中文亂碼可以家後面encode解碼
    data=json.load(response) #出來的答案會和上面一樣，但是此處是利用json套組來處理檔案，上方是以中文解碼
print(data) #取得網址裡面的原始碼
#取得公司名稱
clist=data["result"]["results"] #要抓的資料是來自result底下的results裡面,所以要包兩層
print(clist)
for company in clist:
    print(company["公司名稱"])
#將公司名稱列表出來
with open("data.txt","w",encoding="utf-8") as file: #data.txt是自己新創的檔案
    for company in clist:
        file.write(company["公司名稱"]+"\n")

#公開資料
#適合的資料來源:台北市政府公開資料
#確認資料格式:json?csv?或其他?
