#強制結束迴圈
n=1
while n<5:
    if n==3:
        break
    n+=1
print(n) #印出3
#強制進入下一個迴圈
n=0
for x in [0,1,2,3]:
    if x%2==0:  #如果x被2整除
        continue
    n+=1
print(n)

#加入else運用
n=1
while n<5:
    print("變數n的資料是:",n)
    n+=1
else:
    print(n) #結束迴圈前，印出5(最後一個公式是4+1=5)

for c in "Hello":
    print("逐一取得字串中的字元",c)
else:
    print(c) #結束迴圈前，印出o

#break簡易範例:
m=0
while m<5:
    if m==3:
        break
    print(m) #印出迴圈中的m
    m+=1
print("最後的m是:",m) #印出迴圈結束後的m

#continue的簡易範例:
a=0
for x in [0,1,2,3,4,5]:
    if x%2==0:
        continue #迴圈繼續跑，被二整除的不印出來
    print(x)
    a+=1
print("最後的a是:",a)

#elae簡易範例:
sum=0
for y in range(11):
    sum+=y
else:
    print(sum) #印出1+2+...+10的結果

#綜合範例:找出整數的平方根
k=input("輸入一個整數:")
k=int(k) #int-->整數；float-->可以有小數點
for i in range(k+1):
    if i*i==k:
        print("整數平方根",i)
        break #用break強制結束迴圈十，不會執行else區域
else: #注意!這裡的else跟if不同排，如果同樣縮排會錯誤
        print("沒有整數平方根")

#快捷鍵:ctrl+/ 一次把選取的資料變成備註
#"=="判斷兩個變數之間的"值"是否相同
#"is"式判斷兩個變數之間的"記憶體位置"是否相同