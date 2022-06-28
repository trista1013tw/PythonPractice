#data.size：印出size屬性(總共幾個格子)
#data.shape：2*3的表格--->形狀是2,3
#data.index：索引搜尋

#取得"列"Row(橫向)的資料：
#   1.data.iloc[數字] 根據順序
#   2.data.loc[索引] 根據索引(Series型態)

#取得"欄"Column(直向)的資料：
#   1.data[欄位名稱] 用字典方式直接取得(Series型態)

#建立新欄位：
#data["新欄位名稱"]=列表資料
#data["新欄位名稱"]=Series型態資料
import pandas as pd
data=pd.DataFrame({
    "name":["Amy","Tom","Ross","Kate"],
    "salary":[1000,3000,2000,7000]
}, index=["ㄅ","ㄆ","ㄇ","ㄈ"])
print(data)
print("-------------------------------------------")

print("資料數量",data.size)
print("資料形狀(列,欄)",data.shape)
print("資料索引",data.index)
#以上為基本觀察
print("-------------------------------------------")

print("取得第二列",data.iloc[1], sep="\n")
print("取得第ㄈ列",data.loc["ㄈ"], sep="\n")
print("-------------------------------------------")

print("取得name欄位",data["name"], sep="\n")
names=data["name"]
print("把name全部大寫",names.str.upper(), sep="\n")
salaries=data["salary"]
print("薪資平均",salaries.mean())
print("-------------------------------------------")

#建立新欄位
data["revenue"]=[10000,5000,8000,15000] #data["新欄位名稱"]=列表
data["rank"]=pd.Series([3,2,6,5], index=["ㄅ","ㄆ","ㄇ","ㄈ"])
data["cp"]=data["revenue"]//data["salary"]
print(data)