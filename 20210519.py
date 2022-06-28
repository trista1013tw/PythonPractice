#亂數模組
#載入模組:
import random
#random.choice([0,1,5,8]) #從列表中隨機取1個資料
#random.sample([0,1,5,8],2) #從列表中隨機取2個資料，數字不能超過列表長度
#random.shuffle(data) #將列表的資料"就地"隨機調換順序
#random.random() #取得0.0~1.0之間的隨機亂數，每個數字出現的機率都是相同的
#random.uniform(0.0~1.0) #可以自設範圍，期間出現的數字機率都一樣
#random.normalvariate(100,10) #取得平均數100,標準差10的常態分配亂數，大部分會取到的數字範圍是在90~110之間(平均數+-標準差)

data=random.choice([1,5,6,10,20])
data=random.sample([1,5,6,10,20],3)
print(data)
x=[1,5,8,9,20,33,45]
random.shuffle(x) #洗牌的概念
print(x)
y=random.random()
print(y)
r=random.uniform(0.0,5.0)
print(r)
z=random.normalvariate(100,20)
print(z)

#統計模組
#載入模組:import statistics
#statistics.mean([1,4,6,9]) #計算列表中數字的平均數
#statistics.median([1,4,6,9]) #計算列表中數字中位數
#statistics.stdev([1,4,6,9]) #計算列表中數字的標準差 -->資料散布的狀況

import statistics as st
data=st.mean([1,4,5,8,100])
a=st.median([1,4,6,7,8,100]) #中位數會排除極端值
b=st.stdev([1,2,3,4,5,8,10])
print(data,a,b)

#平均數、中位數、標準差、常態分配