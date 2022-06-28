#if布林值一:
#   若布林值一為True，執行命令(注意:縮排的tab鍵一定要打)
#elif布林值二:
#   若布林值二為True，執行命令
#else:
#   若布林值為False，執行命令
x=input("請輸入數字: ") #取得字串形式的使用者輸入，基本輸入為字串型態
x=float(x) #將字串型態的數字轉換成數字整數
if x>500:
    print("太多了找不開，請問有零鈔嗎?")
elif x>100:
    print("請找錢")
else:
    print("不夠錢")
#int只能運用在整數，小數點指令為float
#四則運算
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
op=input("請輸入運算符號(+,-,*,/): ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("輸入錯誤，請重新再試")
