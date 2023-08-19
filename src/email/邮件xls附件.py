#!/usr/bin/python3

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == '__main__':
    mail163Server = "smtp.163.com"
    mailPort = 25
    mailUserName = "18635572970@163.com"
    mailPasswd = "MMDMTETFGIFHMWHK"

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

    # open里输入添加附件文件的绝对路径
    part = MIMEApplication(open(r'demo.xls', 'rb').read())
    # 构造附件，filename是编辑附件文件名，可以随便写
    part.add_header('Content-Disposition', 'attachment', filename='data.xls')
    # 添加附件
    msg.attach(part)

    ## 发送邮件
    s = smtplib.SMTP()  # 实例化对象
    coneServer = smtplib.SMTP(mail163Server, mailPort)
    coneServer.login(mailUserName, mailPasswd)
    coneServer.sendmail(mailUserName, msg["To"], msg.as_string())
    coneServer.quit()
