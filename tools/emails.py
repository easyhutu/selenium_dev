"""
CREATE: 2018/3/7
AUTHOR: Hehahutu
"""
from framework.logger import logger
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.settings import TIME_TAG, MAIL_HOST, MAIL_USER, MAIL_SMTP_PORT, MAIL_PASS, MAIL_RECEIVER


def send_email(file_path):
    sender = MAIL_USER
    receivers = MAIL_RECEIVER  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEMultipart()

    message['From'] = Header("万店掌测试组", 'utf-8')
    message['To'] = Header("万店掌", 'utf-8')

    subject = '万店掌WEB系统测试报告_{}'.format(TIME_TAG)
    message['Subject'] = Header(subject, 'utf-8')
    with open(file_path, encoding='utf8') as f:
        data = f.read()
    message.attach(MIMEText(data, 'html', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test report_{}.html"'.format(TIME_TAG)
    message.attach(att1)

    try:
        logger.info('...')
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(MAIL_HOST, MAIL_SMTP_PORT)
        logger.info('connect smtp server')
        smtpObj.login(MAIL_USER, MAIL_PASS)
        logger.info('login success')
        smtpObj.sendmail(sender, receivers, message.as_string())
        logger.info('send email success ')
        logger.info('receiver {}'.format(';'.join(MAIL_RECEIVER)))
    except smtplib.SMTPException:
        logger.error('send email failed !!!')


if __name__ == '__main__':
    send_email("""<p>Python 邮件发送测试...</p><p><a href="http://www.runoob.com">这是一个链接</a></p>""")
