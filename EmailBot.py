from cgitb import html
import pandas as pd
import smtplib
from email.message import EmailMessage

 



e = pd.read_excel("path of excel file")
emails = e['Emails'].values

SenderAddress = "yourmail@gmail.com"
password = "your password"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)


subject = "Subject"

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = SenderAddress
msg.set_content("TechnoZ")
msg.add_alternative(f"""\n\n
    write here html codes
    """,   
    subtype ="html")


for email in emails:
    msg['To'] = email
    server.send_message(msg)
server.quit()