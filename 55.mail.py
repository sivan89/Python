import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "lanchumani@gmail.com"
toaddress = "lanchumani@gmail.com"

msg = MIMEMultipart() #creating a `object` from MIMEMultipart to msg 

msg['From'] = fromaddr
msg["To"] = toaddress

msg['Subject'] = "Subject of this mail"

body = "This is a sample enail notification"

msg.attach(MIMEText(body, 'plain'))



s = smtplib.SMTP("smtp.gmail.com", 25) #587 for google , 25 for our org 

s.starttls #TLS for Security

#s.auth()
s.login(fromaddr, getpass.getpass() , initial_response_ok=True)

text = msg.as_string()


s.sendmail(fromaddr, toaddress , text)

s.quit()