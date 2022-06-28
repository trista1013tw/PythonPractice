#列表長度=len(列長)
#list.tuple
grades=[12,60,50,100,23,88,99]
print(grades)
print(grades[0])

grades[0]=0 #把原本編號0的12替換成新的0
print(grades)
grades[1:4]=[] #連續列表中從編號1到編號3(不包含4)的資料
print(grades)
grades=grades+[33,44,55,66] #列表串接(簡單加法)
print(grades)

length=len(grades) #取得列表長度 len(列表資料)
print(length)

data=[[3,6,9,12],[2,4,6,8,10]]
print(data[1][2]) #前面的大框框是選擇哪一個數列，第二個框框選擇的是被選擇數列裡面的編號

do=(3,4,5,6,8,9)
print(do[0:2])
#do[0]=0 
#在Tuple中不能取代及變動原來資料，22行會產生錯誤
print(do)

#集合的運算
s1={3,4,5,6,7,8,9}
print(3 in s1)
print(100 in s1)
print(99 not in s1)
print(5 not in s1)
s2={2,3,4}
s3=s1&s2 #&(交集):取兩個集合中，相同的資料
print(s3)
s4=s1|s2 #|(聯集):取兩個集合中的所有資料，但不重複
print(s4)
s5=s1-s2 #-(差集):從s1中，減去和s2中有重疊的部分-->似減法
print(s5)
s6=s1^s2 #^反交集:取兩個集合中，不重疊的部分
print(s6)

s=set('hello') #set字串會自動幫我們拆解成集合，但是相同的字不會出現兩次
print(s)
o=set('我愛你媽媽!')
print(o)

#字典的運算:key-value配對
dic={"apple":"蘋果","紅色":"red"}
dic['apple']='小蘋果'
print(dic["apple"])

#判斷key是否存在(以key判斷，不是以value)
print('紅色' in dic)
print('red' not in dic)
print(dic)
del dic['apple'] #刪除字典中的鍵值對(key-value pair)
print(dic)

#進階 從列表資料產生字典
cd={x:x*2 for x in [3,4,5]} #for...in用法固定，後面的列表可以替換
print(cd)