import smtplib
import configparser

class MailSender():
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read("conf.conf")
        self.user = self.cfg.get("MAIL","user")
        self.password = self.cfg.get("MAIL","pswd")
        self.message="Subject: This is a test email.\n\nThis is the body of the test email."
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(str(self.user), str(self.password))
    
    def send(self,message,receiver):
        res=self.server.sendmail(self.user, receiver, message)
        return (res)

# C= MailSender()
# do_kogo="skibinskihubert@o2.pl"
# C.send("Subject: This is a test email.\n\nThis is the body of the test email.",do_kogo)


