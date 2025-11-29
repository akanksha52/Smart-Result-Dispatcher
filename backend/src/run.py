import os
import time
import argparse
from generate_pdf import generateReport
from mailer import renderTemplate, sendEmail
from utils import readStudents, logSend
from pathlib import Path

baseDir=Path(__file__).resolve().parents[1]
outputDir=baseDir/"output"/"reports"
templateDir=baseDir/"templates"

def main(csvFile):
    students=readStudents(csvFile)
    for s in students:
        try:
            pdfPath=generateReport(s)
            html=renderTemplate(templateDir, s)
            subject=f"Your exam result: {s.get("name")}"
            sendEmail(s.get("email"), subject, html, pdfPath)
            print(f"Sent to {s.get('name')} <{s.get('email')}>")
            logSend(s.get("name"), s.get("email"), "Sent", "")
            time.sleep(2)
        except Exception as e:
            print("Error for", s.get("name"), e)
            logSend(s.get('name'), s.get('email'), "failed", str(e))
            
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("csv", help="path to students csv")
    args=parser.parse_args()
    main(args.csv)