from smtplib import SMTP
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

class Mail_Helper:
    _name = 'robot'
    # 构造器模式 初始化附件邮件
    message = MIMEMultipart()
    message_text = None


    def init(self):
        self.message = MIMEMultipart()
        self.message_text = None
    
    def message_builder(self,message):
        text_content =  MIMEText(message, 'plain', 'utf-8')
        self.message_text = text_content
    
    def file_builder(self,path,name='unknown'):
        with open(path,'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment',filename= name +'.png')
            part.add_header('Content-Type', 'image/png')
            self.message.attach(part)
    def header_builder(self,receiver,subject):
        message = self.message
        message['From'] = Header('x <mail>')
        message['To'] = receiver
        message['Subject'] = subject
    def send_mail(self,receiver):
        self.message.attach(self.message_text)
            # 创建SMTP对象
        smtper = SMTP('smtp.qq.com',587)
        # 开启安全连接
        # smtper.starttls()
        sender = 'user'
        receiver = receiver
        smtper.login(sender, 'key')
        # 发送邮件
        smtper.sendmail(sender, receiver, self.message.as_string())
        # 与邮件服务器断开连接
        smtper.quit()
        print('发送完成!')
        self
        
        





# example
# if __name__ == '__main__':
#     mail = Mail_Helper()
#     mail.header_builder('852040420@qq.com','这是一段标题')
#     mail.message_builder('这是一段内容')
#     mail.file_builder('./test.png','test.png')
#     mail.send_mail()
