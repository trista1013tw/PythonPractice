#h參數的預設資料:
#def函式名稱(參數名稱=預設資料):
#   函式內部的程式碼
def say(msg="Hello"):
    print(msg)
say("Hello Function") #-->印出參數資料Hello Function
say() #-->沒有參數資料，印出預設值Hello

def power(base,exp=0): #-->次方的重要參數:Ex 3的平方,(base=3,exp=2)
    print(base**exp)
power(3,2)
power(4) #因為預設值exp=0，所以沒有打上幾次方會直接帶入預設值0次方

#def 函式名稱(名稱1,名稱2):
#   函式內部程式碼
#呼叫函釋,以參數名稱對應資料
#函式名稱(名稱2=3,名稱1=5)  -->我們可以不管順序，直接用名稱對應參數
def divide(n1,n2):
    result=n1/n2
    print(result) #此處如果改成print(n1/n2)也可以
divide(2,4)
divide(n2=2,n1=4)

#def 函式名稱(*無限參數): -->*不定常數
#   無限參數以Tuple資料型態處理
#   函式內部的程式碼
#呼叫函示可以傳入無限量的參數
#函式名稱(資料一,資料二,資料三)
def say(*msgs):
    for msg in msgs:
        print(msg)
say("Hell","Arbitrary","Argument")

def avg(*ns):
    sum=0 #開頭是從0開始，平均才不會多加
    for n in ns:
        sum=sum+n
        print(n)
    print(sum/len(ns)) #len()相當於一個數列的長度(有幾個數字)
    print(ns)
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)