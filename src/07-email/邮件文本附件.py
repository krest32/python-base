#!/usr/bin/python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == '__main__':
    mail163Server = "smtp.163.com"
    mailPort = 25
    mailUserName = "18635572970@163.com"
    mailPasswd = ""

    msg = MIMEMultipart()
    msg["Subject"] = "带有附件的邮件"
    msg["From"] = mailUserName  # 发送人
    msg["To"] = "krest2021@163.com"  # 接收人

    # 邮件正文
    content = '''
    这是一封带有附件的邮件...
    有1个附件
    '''
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    # 构造附件1，txt文件
    att1 = MIMEText('附件内容', 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    msg.attach(att1)


    ## 发送邮件
    s = smtplib.SMTP()  # 实例化对象
    coneServer = smtplib.SMTP(mail163Server, mailPort)
    coneServer.login(mailUserName, mailPasswd)
    coneServer.sendmail(mailUserName, msg["To"], msg.as_string())
    coneServer.quit()
