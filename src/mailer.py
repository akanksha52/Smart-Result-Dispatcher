import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()
smtpServer=os.getenv("smtpServer")
smtpPort=int(os.getenv("smtpPort", "587"))
smtpUser=os.getenv("smtpUser")
smtpPass=os.getenv("smtpPass")
fromName=os.getenv("fromName", "Result dispatch")




