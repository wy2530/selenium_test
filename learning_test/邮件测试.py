import smtplib
# import os, time, datetime
# from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'wangyang_jocelyn@126.com'  # 发件人
receiver = 'selenium_test_2020@126.com'  # 收件人

# 为安全找想,设置客户端授权码，不是密码
auth_code = 'OUIFPFXKUXDOHQZI'
# 主题
subject = '自动化测试报告'

# 读取文件内容
f = open("./result.html", 'rb')
mail_body = f.read()
f.close()

# HTML 形式的文件内容
html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
html['Subject'] = subject
html['from'] = sender
html['to'] = receiver

# html附件 将测试报告放在附件中发送(因为再邮箱中自动打开有点问题)
att1 = MIMEText(mail_body, 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'  # 协议规范
att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 文件名称

# 构建发送与接收信息
msg = MIMEMultipart()
msg['Subject'] = subject

msg['from'] = sender
msg['to'] = receiver
msg.attach(html)  # 将html附加在msg里
msg.attach(att1)

# 连接 登录 上smtp服务器
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(sender, auth_code)
# 发送邮件
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
