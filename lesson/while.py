#while迴圈
#while 布林值:
#   若布林值為True，執行命令
#   回到上方，做下一次的迴圈判斷
n=1
while n<5:
    print("變數n的資料是:",n)
    n+=1
m=1
sum=0
while m<=3:
    print(m)
    m+=m
print(sum)

#for迴圈
#for變數名稱in列表或字串:
#   將列表中的項目或字串中的字元逐一取出，逐一處裡
for x in [4,1,2,5]:
    print("逐一取得列表中的資料:",x)
#for 變數名稱 in range(3): 相當於 for 變數名稱 in [0,1,2]:
#range() :幫忙產生連續的數列
#for 變數名稱 in range(3,6)=[3,4,5]-->有定義開頭結尾，開頭包含，結尾不包含
#crtl+c可以強制停止跑系統
for x in [3,5,1]:
    print(x)
for z in "hello":
    print(z)
for y in range(1,11):
    print(y) #沒有這個(1~10的列表)不影響最後sum的加總
    sum=sum+y
print(sum)
