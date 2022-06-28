#模組:
#獨立的程式檔案，將程式寫在一個檔案中，此檔案可重複載入使用
#載入>使用:先載入模組，再使用模組中的函式或變數

#import 模組名稱
#import 模組名稱 as 模組別名

#模組名稱或別名.函式名稱(參數資料)
#   模組名稱或別名.變數名稱        -->使用模組

#內建模組:
import sys
print(sys.platform) #印出作業系統
print(sys.maxsize) #印出整數型態的最大值
print(sys.path) #印出搜尋模組路徑
print("--------------------------------------")

#調整搜尋模組路徑
import sys
#sys.path.append("modules") #-->加入新的路徑，讓新資料夾的模組也能使用
print(sys.path)
import geometry
print(geometry.distance(1,1,5,5))

#自訂的模組:
#建立幾何運算模組:建立檔案geometry.py,定義平面幾何運算用的函式
#載入geometry模組,並使用模組中定義的功能
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)

