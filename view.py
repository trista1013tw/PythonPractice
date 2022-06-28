#使用jason格式讀取、複寫檔案
import json
#從檔案中讀取json資料，放入變數data裡面
with open("config.json", mode="r") as view:
    data=json.load(view)
print(data) #data是一個字典資料
#print("name",data["name"])
#print("version",data["version"])
data["name"]="OMG" #修改變數中的資料
#把新的資料複寫更新到檔案中
with open("config.json", mode="w") as view:
    json.dump(data,view)

#本來的Name被修改成New name