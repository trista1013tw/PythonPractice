#開啟檔案
#檔案物件=open(檔案路徑,mode=開啟模式)
#開啟模式:讀取模式-r、寫入模式-w、讀寫模式-r+
#讀取文字:
#檔案物件.read()
#一次讀取一行
#for 變數 in 檔案物件:
#with open("data.txt",mode="r",encoding="utf-8") as file:
 #   data=file.read()
#print(data)
#import json
#讀取到的資料=json.load(檔案物件)

#寫入(儲存)檔案
#檔案物件.write(字串)
#字串中換行用 \n

#import jason
#jason.dump(要寫入的資料,檔案物件)


#file=open("data.txt",mode="w",encoding="utf-8") #開啟
                               #encoding="utf-8"-->沒有會導致中文亂碼
#file.write("321") #操作
#file.close() #關閉


#關閉檔案
#檔案物件.close()
with open("data.txt",mode="w",encoding="utf-8") as file:
   file.write("123\n321\n666\n777")

#最佳實務
#with open(檔案路徑,mode=開啟模式) as 檔案物件:
#   讀取或寫入檔案程式
#以上區域會自動、安全的關閉檔案

#把檔案中的數字資料，一行一行的讀取出來，並計算總合


sum=0
with open("data.txt",mode="r",encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)

