import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_confirm_email(email: str):
    read_docs = open('/home/nia/Desktop/projects/alarmer/alarmer/mailing.txt', 'r').read().split()
    sender = read_docs[0]
    password = read_docs[1]
    mail_object = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    msg = MIMEMultipart('alternative')
    html = '''
    are u succesfuly registrate on this website
    last step: please confirm ur email addres
    <a href="http://www.my_site.com/confirm/"><button>Confirming</button></a>
    '''
    part = MIMEText(html, 'html')
    msg.attach(part)
    mail_object.login(sender, password)
    mail_object.sendmail(sender, email, str(msg))
    mail_object.quit()