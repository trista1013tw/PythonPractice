import email.message
#msg["From"]="寄件人地址"
#msg["To"]="收件人地址"
#msg["Subject"]="電子郵件主題"
#加入純文字內容：msg.set_content("文字內容")
#加入HTML內容：msg.add_alternative("<h3>HTML內容</h3>",subtype="html")
msg=email.message.EmailMessage()
msg["From"]="ok8426888@gmai.com"
msg["To"]="ok8426888@gmail.com"
msg["Subject"]="Hello Tina"

msg.set_content("測試python寄信 \n 哈哈哈")
#msg.add_alternative("<h3>優惠券</h3>滿五百送一百呦~",subtype="html")

import smtplib
#從網路上找到主機名稱和連接埠號：server=smtplib.SMTP_SSL("主機名稱",連接埠號)
#驗證身分：server.login("帳號","密碼")
#寄送電子郵件：server.send_message(msg)
#發送完畢關閉連線：server.close()
#到網路上搜尋gmail smtp server或是yahoo smtp server
server=smtplib.SMTP_SSL("smtp.gmail.com", 465) #465為google端口
server.login("ok8426888@gmail.com","x159357555")
server.send_message(msg)
server.close()