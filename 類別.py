#類別
#封裝的變數或函式，統稱類別的屬性
#定義>使用:要先建立(定義)類別,然後才能使用類別中封裝的屬性

#定義類別
#class 類別名稱:(注意:類別名稱第一個字母大寫)
#   定義封裝的變數
#   定義封裝的函式
class Test: #定義Test類別
    x=3 #定義變數
    def say(): #定義函式
        print("Hello")
#定義一個類別IO,有兩個屬性supportedScrs和read
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported.")
        else:
            print("Read from",src)

#使用類別:
#類別名稱.屬性名稱
Test.x+3 #取得屬性x的資料3
Test.say() #呼叫屬性say函式

print(IO.supportedSrcs)
IO.read("file") #因為file是程式支援的，所以會跑出read from file
IO.read("internet") #python不支援internet