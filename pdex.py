import pandas as pd
data=pd.read_csv("googleplaystore.csv") #把csv格式的檔案讀取成一個DataFrame
# print("資料數量：",data.shape, sep="\n")
# print("資料欄位：",data.columns, sep="\n")

#condition=data["Rating"]<=5
#data=data[condition]
#print("前一千個平均數",data["Rating"].nlargest(1000).mean(), sep="\n") #前一千個最高分的平均成績
#print("中位數",data["Rating"].median(), sep="\n")


#print(data["Installs"][10472])
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
# print("平均數",data["Installs"].mean())
# condition=data["Installs"]>100000
# print("安裝數量大於10萬的平均數",data[condition].shape[0])

keyword=input("輸入關鍵字：")
condition=data["App"].str.contains(keyword, case=False) #case=False指令忽略大小寫
print("包含關鍵字的應用程式數量：",data[condition]["App"].shape[0])