import pandas as pd
data=pd.Series([30,100,60])
#用Series篩選
condition=[True,False,True]
filteredData=data[condition]
print(filteredData)

#用條件篩選
condition=data>=60
print(condition)
filteredData=data[condition]
print("考試成績及格",filteredData)

print("-------------------------------------")

data=pd.Series(["您好","Python","Pandas"])
condition=data.str.contains("P")
print(condition)
filteredData=data[condition]
print(filteredData)

print("-------------------------------------")

data=pd.DataFrame({
    "name":["Amy","Tom","Ross","Kate"],
    "salary":[1000,3000,2000,7000]
}, index=["ㄅ","ㄆ","ㄇ","ㄈ"])
print(data)
condition=data["salary"]>5000
print(condition)
Data=data[condition]
print(Data)
print("-------------------------------------")

condition=data["name"].str.contains("m")
print(condition)
Data=data[condition]
print(Data)