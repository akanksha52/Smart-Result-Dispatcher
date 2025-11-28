import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from jinja2 import Template
import mimetypes

envPath=r"C:\Users\akank\Desktop\automation\9 Smart Result dispatcher\.env"
load_dotenv(envPath)
smtpServer=os.getenv("smtpServer")
smtpPort=int(os.getenv("smtpPort", "587"))
smtpUser=os.getenv("smtpUser")
smtpPass=os.getenv("smtpPass")
fromName=os.getenv("fromName", "Result dispatch")

def renderTemplate(templatePath: str, context: dict) -> str:
    with open(templatePath, "r", encoding="utf-8") as f:
        tpl=Template(f.read())
    return tpl.render(**context)

def sendEmail(toEmail: str, subject: str, htmlBody: str, attachedPath: str=None) :
    msg=EmailMessage()
    msg["Subject"]=subject
    msg["From"]=f"{fromName} <{smtpUser}>"
    msg["To"]=toEmail
    msg.set_content("This is an HTML email. Please use an HTML-capable email client.")
    msg.add_alternative(htmlBody, subtype="html")
    
    if attachedPath:
        with open(attachedPath, "rb") as f:
            data=f.read()
            ctype, encoding=mimetypes.guess_type(attachedPath)
            if ctype is None:
                ctype="application/octet-stream"
            mainType, subType=ctype.split("/", 1)
            msg.add_attachment(data, maintype=mainType, subtype=subType,
                           filename=os.path.basename(attachedPath))
            
    with smtplib.SMTP(smtpServer, smtpPort) as smtp:
        smtp.ehlo()
        if smtpPort==587:
            smtp.starttls()
            smtp.ehlo()
        smtp.login(smtpUser, smtpPass)
        smtp.send_message(msg)
