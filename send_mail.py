import smtplib
from email.mime.text import MIMEText

def mail():

    host = 'smtp.163.com'  # 设置发件服务器地址
    port = 25  # 设置发件服务器端口号，这里有SSL和非SSL两种形式
    sender = 'printhello@163.com'
    password = '********'
    receiver = 'wwt1121@163.com'
    body = '<h1>Hi</h1><p>test</p>' # 设置邮件正文，这里是支持HTML的
     
    msg = MIMEText(body, 'html') # 设置正文为符合邮件格式的HTML内容
    msg['subject'] = 'Hello world' # 设置邮件标题
    msg['from'] = sender  # 设置发送人
    msg['to'] = receiver  # 设置接收人
     
    try:
        s = smtplib.SMTP(host, port)  # 如果是使用SSL端口，这里就要改为SMTP_SSL
        s.login(sender, password)  # 登陆邮箱
        s.sendmail(sender, receiver, msg.as_string())  # 发送邮件！
        print('Done')
    except smtplib.SMTPException:
        print('Error')

if __name__ == '__main__':
    mail()