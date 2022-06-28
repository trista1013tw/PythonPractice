x="pqrs"
for i in range(len(x)):
    x[i].upper()
print(x)
x=x.upper()
print(x)

myTulpe=[x for x in range(1,6,1)]
print(myTulpe)

def fun(name,age=20):
    print(name,age)
fun('Emma',25)

#import camelcase
#c=camelcase.CamelCase()
#txt="python hub"
#print(hump(txt))

l=["a","A","B"]
l.sort()
print(l)

#l=[1,2]
#l+=3
#print(l)

a,b=2,3
c=a**b**a
print(c)

l=[1,2,["a","b",["cat","dog"],"c"],3]
print(l[2][2][0][2])

from math import *
a,b=2.99,-3.1
print(int(a),fabs(b))

a=True
b=False
print(a or a and b)

r=[1,2,2,3,4,5]
s=set(r)
t=[1,2,3]
print(sum(t))
print(len(s)+sum(t))

tuple1=(1,2,4,3)
tuple2=(1,2,3,4)
print(tuple1>tuple2)

i=0
while i<5:
    print(i,end=" ")
    i+=1
    if i==3:
        break
else:
    print(0)

#mylist=["python","hub"]
#for i in mylist:
#    mylist.append(i.upper())
#print(mylist)
#如果把print放外面會變成沒有回應，放在裡面會無限輪迴

def fun():
    pass
    print("python.hub")
fun()

def fun():
    pass
print(type(fun()))

print(bool(False),end=" ")
print(bool())

myDict={1:"a",2:"b",3:"c"}
m=myDict.pop(1)
print(m)
print(myDict)

def fun():
    for x in range(22,23,24):
        print(x)
fun()

s=list((23,)*4)
print(s)

x=set('abc') 
x.add('def')
print(x)
#for first x=set('abc') it's creates a set of random arrangement of a,b,c
#as set arrange elements in random series so no particular position is alloted to any string or number in the set.
#set() 函数创建一个无序不重复元素集
import urllib.request as req
src="https://www.ptt.cc/bbs/Gossiping/index.html" #--->如果要抓其他頁的資料，這邊要先刪除不然跑不到別頁去
request=req.Request(src,headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

    #解析原始碼，取得文章標籤
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")
for title in titles:
    if title.a !=None:
        print(title.a.string)