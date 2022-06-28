#程式區塊
#函式:程式碼包裝在一個區塊中，方便隨時呼叫使用-->參數讓我們的函式富有彈性
#定義>呼叫:要先定義(建立)函式，然後才能呼叫(使用)函式

#def函式名稱(參數名稱、名字):
#   函式內部程式碼

#定義一個印出Hello的函式
def sayHello():
    print("Hello")
#定義可以印出任何資訊的函式
def say(msg):
    print(msg)
    return
#定義一個可以做加法的函示
def add(n1,n2):
    result=n1+n2
    print(result)

#基本語法:函式名稱(參數資料)
sayHello()
say("Hello Function")
say("Hello python")
add(3,4)
add(7,8)

#回傳值
#基本語法:
#def 函式名稱(參數名稱):
#   函式內部的程式碼
#   return -->結束函式，回傳None / return 資料-->結束函式，回傳"資料"-->其中"資料"可以替換成字典或其他東西
value=say("Hello Function") #此處就是回傳值
print(value) #印出None

def add(n1,n2):
    result=n1+n2
    print(result)
    return"OMG"
value=add(3,4)
print(value)   #-->此範例程式會算出add總和是7，但是印出來的資料會是return後面的資料