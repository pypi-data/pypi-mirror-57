"""封装发送邮件类"""
import os
import time

# 导入邮件模块
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendMail:
    def __init__(self, report_path, smtp_server, sender, password, receiver, email_subject, project_name):
        """
        发送邮件初始化
        :param report_path: 取报告的路径，拼接到result文件夹下的report路径即可
        :param smtp_server:smtp_server
        :param sender:发件人
        :param password:密码
        :param receiver:收件人
        :param email_subject:邮件主题
        :param project_name:邮件名称
        """
        self.file_path = report_path
        self.smtp_server = smtp_server
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.email_subject = email_subject
        self.project_name = project_name

    # 2.定义：取最新测试报告
    def new_file(self):
        # 列举test_dir目录下的所有文件，结果以列表形式返回。
        lists = os.listdir(self.file_path)
        # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
        # 最后对lists元素，按文件修改时间大小从小到大排序。
        lists.sort(key=lambda fn: os.path.getmtime(self.file_path + '\\' + fn))
        # 获取最新文件的绝对路径
        report_path = os.path.join(self.file_path, lists[-1])
        #    L=file_path.split('\\')
        #    file_path='\\\\'.join(L)
        return report_path

    def send_mail(self):
        file_path = self.new_file()
        f = open(file_path, 'rb')
        # 读取测试报告正文
        mail_body = f.read()
        f.close()
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        try:
            smtp = smtplib.SMTP(self.smtp_server, 25)
            smtp.login(self.sender, self.password)
            msg = MIMEMultipart()
            # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
            # 发送正文
            text = MIMEText(mail_body, 'html', 'utf-8')
            # 定义邮件正文标题
            text['Subject'] = Header(self.project_name + '自动化测试报告', 'utf-8')
            msg.attach(text)
            # 发送附件
            # Header()用于定义邮件主题，主题加上时间，是为了防止主题重复，主题重复，发送太过频繁，邮件会发送不出去。
            msg['Subject'] = Header(self.email_subject + self.project_name + '自动化测试报告' + now, 'utf-8')
            msg_file = MIMEText(mail_body, 'html', 'utf-8')
            msg_file['Content-Type'] = 'application/octet-stream'
            msg_file['Content-Disposition'] = 'attachment; filename="{projectName} Report {now}.html"'.format(
                projectName=self.project_name, now=now)
            msg.attach(msg_file)
            # 定义发件人，如果不写，发件人为空
            msg['From'] = self.sender
            # 定义收件人，如果不写，收件人为空
            msg['To'] = self.receiver
            smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
            smtp.quit()
            return True
        except smtplib.SMTPException as e:
            print(str(e))
            return False

