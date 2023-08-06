import logging

import smtplib
from email.header import Header
from email.mime.text import MIMEText

from alerta.plugins import PluginBase

LOG = logging.getLogger('alerta.plugins')


class NotifyTestReceiver(PluginBase):
    """
    Default heartbeat receiver intercepts alerts with event='Heartbeat', converts
    them into heartbeats and will return a 202 Accept HTTP status code.
    """

    def pre_receive(self, alert, **kwargs):

        print('######################### plugin notify_test.py alert.event:', alert.event)
        print('######################### plugin notify_test.py alert.origin:', alert.origin)
        print('######################### plugin notify_test.py alert.customer:', alert.customer)
        print('######################### plugin notify_test.py alert.tags:', alert.tags)

        return alert

    def post_receive(self, alert, **kwargs):
        print('######################### plugin notify_test.py post_receive:', alert.tags)
        mail_host = "smtp.163.com"  # SMTP服务器
        mail_user = "pengtaoman"  # 用户名
        mail_pass = "pt--750926PT"  # 授权密码，非登录密码

        sender = 'pengtaoman@163.com'
        receivers = 'pengtaoman@163.com'

        content = 'alertad notification!!!'
        title = alert.event

        message = MIMEText(content, 'plain')  # 内容, 格式, 编码
        message['From'] = sender
        message['To'] = receivers
        message['Subject'] = title

        try:
            smtpObj = smtplib.SMTP(mail_host, 25)  # 启用SSL发信, 端口一般是465
            smtpObj.login(mail_user, mail_pass)  # 登录验证
            messsss = message.as_string()
            smtpObj.sendmail(sender, receivers, messsss)  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)
        return

    def status_change(self, alert, status, text, **kwargs):
        print('######################### plugin notify_test.py status_change:', alert.tags)
        return

    def take_action(self, alert, action, text, **kwargs):
        print('######################### plugin notify_test.py take_action:', alert.tags)
        return alert
