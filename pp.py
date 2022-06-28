#Pandas：概念類似試算表的資料分析套件。
#Series：就像是一個列表、或是試算表中直向的欄位資料
#DataFrame：就像是一個表格，有欄有列的概念

#載入Pandas模組
import pandas as pd
#data=pad.Series(列表)
#data.max() --->找最大值
#data.median()  --->計算中位數
#data=data*2  --->放大兩倍
data=pd.Series([20,10,15])
print(data.max(),data.median(),data*2)
data=data==20 #==:裡面有沒有符合數值是20的資料
print(data)


#以字典資料為底，建立DataFrame
#data=pd.DataFrame(字典)
#data["欄位名稱"] --->取得特
#data.iloc[列編號] --->列編號按順序由0開始累加
data=pd.DataFrame({
    "name":["Amy","Tom","Bob"],
    "salary":[30000,70000,50000]
})
print("--------------------------------------------")
print(data.iloc[1])