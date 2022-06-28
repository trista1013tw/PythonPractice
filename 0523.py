#1.類別與類別屬性
#2.類別與實體物件、實體屬性(V)

#先定義類別，再透過類別建立實體物件
#先建立實體物件，才能使用實體屬性
#初始化函式--> def__init__(self):
#呼叫初始化函式-->obj=類別名稱()

#class Point:
#    def __init__(self):
#        self.x=3 #建立實體物件
#        self.y=4 #此實體物件包含x和y兩個實體屬性
#p=Point()

#class Point:
#    def __init__(self,x,y): #self固定帶入，後面還可以再放參數
#        self.x=x
#        self.y=y
#p=Point(1,5) #1對應x，5對應y

#基本語法: 實體物件.實體屬性名稱
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p=Point(1,5)
print(p.x+p.y)

#dot實體物件的設計:平面座標上的點
class dot:
    def __init__(self,x,y): #一定要self
        self.x=x #x,y實體屬性
        self.y=y
#建立第一個實體物件
d1=dot(3,4)
print(d1.x,d1.y)
#健立第二個實體物件
d2=dot(5,6)
print(d2.x,d2.y)

#Fullname實體物件的設計:分開紀錄性、明資料的全名
class Fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=Fullname("C.W.","Peng")
print(name1.first,name1.last)
name2=Fullname("T.Y.","White")
print(name2.first,name2.last)

class size:
    def __init__(self,long,width,hight):
        self.long=long
        self.width=width
        self.hight=hight
s1=size(3,4,5)
print(s1.long,s1.width,s1.hight)

#Point實體物件設計:平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def distance(self, targetX, targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
p=Point(3,4)
p.show()
result=p.distance(0,0) #計算座標3,4與座標0,0的距離
print(result) #因為結果是用return回傳，所以需要利用額外的店數接受回傳的數值

class File:
    #定義初始化屬性
    def __init__(self, name):
        self.name=name
        self.file=None #尚未開啟檔案:初始是None
    #實體方法
    def open(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1=File("data1.txt")
f1.open() #打開
data=f1.read() #讀取
print(data)
#讀取第二個檔案
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)

f3=File("data.txt")
f3.open()
data=f3.read()
print(data)