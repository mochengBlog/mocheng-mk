#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "llmoyueqingcheng@163.com"  # 邮箱用户名
mail_pass = ""  # 是邮箱授权口令，不是邮箱登录密码

sender = "llmoyueqingcheng@163.com"  # 发送邮件邮箱
receivers = ["todo@mail.dida365.com"]  # 接收邮件，可添加多个邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')  # 发送邮件的内容、类型
message['From'] = sender  # 邮件发信人，也可以自己定义，建议和发件人一致
message['To'] = receivers[0]  # 邮件收件人，可自己定义，建议和收件人一致

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # SMTP端口号25，pop3端口号110
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")