#定義函式
def multiply(n1,n2):
    print(n1*n2)   #函式內部程式碼，若是沒有呼叫就不會執行
    return 10

#呼叫函式
n1=input()
n1=int(n1)
n2=input()
n2=int(n2)
multiply(n1,n2)

value=multiply(3,4)
print(value)

#程式的包裝
sum=0
for x in range(11):
    sum+=x
print(sum)

def calculate():
    sum=0
    for n in range(21):
        sum+=n
    print(sum)   
calculate()
