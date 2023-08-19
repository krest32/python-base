# 与邮件发送有关的模块
import smtplib
# 在设置邮件的主题、内容时需要用到的模块
from email.mime.text import MIMEText
if __name__ == '__main__':

    # 163邮箱的服务器地址，如果需要实现用其它邮箱实现发送
    # 邮件，这里需要改为其它邮箱的服务器地址
    mail163Server = "smtp.163.com"
    # 163邮箱的端口
    mailPort = 25
    # 163邮箱的用户名
    mailUserName = "18635572970@163.com"  # 这里设置自己的邮箱的用户名
    # 163邮箱的密码，注意：不是登录密码，而是授权密码
    # 授权密码的设置步骤:登录--》设置--》POP3/SMTP/IMAP--》客户端授权密码
    # 设置了授权密码后，记得回到POP3/SMTP/IMAP中把最上面两个的勾打上
    mailPasswd = ""  # 自己设置的授权密码

    # 设置邮件收件人
    to_mail = "krest2021@163.com"

    # 连接服务器，通过smtplib.SMTP()连接
    # 第一个参数是邮箱服务器地址，第二个参数是邮箱服务器的端口
    conneServer = smtplib.SMTP(mail163Server, mailPort)

    # 登录邮箱
    conneServer.login(mailUserName, mailPasswd)

    # 创建邮件
    msg = MIMEText("测试邮件内容")

    # 设置主题,下面的必须为Subject，不能自己随意更改
    # 以下的三个内容必须设置，否则容易出现554的错误
    msg["Subject"] = "测试邮件标题"

    # 设置发件人
    msg["From"] = mailUserName

    # 设置收件人
    msg["To"] = to_mail

    # 发送邮件
    conneServer.sendmail(mailUserName, to_mail, msg.as_string())

    # 发送完后必须关闭,否则浪费空间资源
    conneServer.close()
