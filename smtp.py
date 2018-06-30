#coding=utf-8
import smtplib
from email.mime.text import MIMEText
msg_from='2233597809@qq.com'                                 
passwd='vqegsxbzuwsgecid'                                  
msg_to='1252692433@qq.com'                                 
                            
subject="来自沈理第一强者的问候"                                         
content="张宇准备接受大华哥的制裁吧"
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except smtplib.SMTPException:
    print ("发送失败")
finally:
    s.quit()
