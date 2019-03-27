# coding:utf-8

import smtplib
from email.mime.text import MIMEText

mail_user = 'ctf_dicha@21cn.com'
mail_pass = '634DRaC62ehWK6X'
mail_server = 'smtp.21cn.com'
mail_port = 465
to_user = 'wyd0n9@gmail.com'


def send_mail(title, content):
    # 创建一个实例，这里设置为html格式邮件
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    msg['Subject'] = title
    msg['From'] = mail_user
    msg['To'] = to_user
    try:
        # 登录smtp服务器
        server = smtplib.SMTP_SSL(mail_server, mail_port)
        server.login(mail_user, mail_pass)
        # 邮件发送
        server.sendmail(mail_user, to_user, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(str(e))
        return False
