import smtplib
import configparser

class MailSender():
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read("conf.conf")
        self.user = self.cfg.read("Mailing","user")
        self.password = self.cfg.read("Mailing","pswd")
        self.message="Subject: This is a test email.\n\nThis is the body of the test email."
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.user, self.password)
    
    def send(self,message,receiver):
        res=self.server.sendmail(self.user, receiver, message)
        print(res)

C= MailSender()
do_kogo=""
C.send("Subject: This is a test email.\n\nThis is the body of the test email.",do_kogo)
