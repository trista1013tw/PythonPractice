#Panda資料索引：資料的獨立編號(就像試算表中最左邊的編號)
#內建索引：以列表資料為底，建立Series
#   pd.Series(資料列表)
#自訂索引：
#   pd.Series(資料列表,index=索引列表)
import pandas as pd
#觀察資料：
#dtype --->資料的型態
#size --->資料的數量
#index --->資料的索引

#取得資料：
#data[順序]
#data[索引]

#數字資料常用：
data=pd.Series([3,10,20,5,-12])
print(data.sum(),data.max(),data.prod()) #data.prod()乘法總和
print(data.mean(),data.median(),data.std())
print(data.nlargest(3),data.nsmallest(2)) #data.nlargest(3)找出最大的3個數字是；data.nsmallest(2)找出最小的2個數字是?
print("-------------------------------------------")
#字串資料常用：(各種字串的操作，都定義在str底下)
data=pd.Series(["您好","Python","Pandas"])
print(data.str.lower(),data.str.upper(),data.str.len())  #所有字串小寫、大寫、取得字串長度
print(data.str.cat(sep=","),data.str.contains("P"))  #把字串用逗號串在一起、判斷自傳中是否包含P
print(data.str.replace("您好","Hello"))  #字串取代
print("-------------------------------------------")

data=pd.Series([5,4,-2,7,3],index=["a","b","c","d","e"])  #改變資料索引123改成abc
print("資料的型態",data.dtype)
print("資料的數量",data.size)
print("資料的索引",data.index)

print("-------------------------------------------")
print("最大值",data.max())
print("總和",data.sum())
print("標準差",data.std())
print("中位數",data.median())
print("最大的前三個數",data.nlargest(3))
print("-------------------------------------------")
data=pd.Series(["您好","歡迎光臨","Python","Pandas"])
print(data.str.lower())
print(data.str.upper())
print(data.str.len())
print(data.str.cat(sep="."))
print(data.str.contains("好"))
print(data.str.replace("您好","您們好"))