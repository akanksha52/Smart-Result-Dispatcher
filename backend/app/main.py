from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import shutil, os
from pathlib import Path

from src.generate_pdf import generateReport, generateAllPdfs
from src.mailer import renderTemplate, sendEmail, sendAllEmails
from src.utils import readStudents, logSend

app=FastAPI(title="Smart Result Dispatcher API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

dataDir=Path(__file__).resolve().parents[1]/"data"
reportsDir=Path(__file__).resolve().parents[1]/"output"/"reports"
logFile=Path(__file__).resolve().parents[1]/"logs"

@app.post("/upload-csv")
async def uploadCsv(file: UploadFile=File(...)):
    dest=dataDir/"studentscsv"
    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"status": "ok", ".saved": str(dest)}

@app.post("/generate-pdfs")
def generate_pdfs(background: BackgroundTasks):
    background.add_task(generateAllPdfs)
    return {"status": "PDF generation started"}

@app.post("/send-emails")
def send_emails(background: BackgroundTasks):
    background.add_task(sendAllEmails)
    return {"status": "started"}

@app.get("/reports")
def getReports():
    files=[f.name for f in reportsDir.glob("*.pdf")]
    return {"reports": files}

@app.get("/logs")
def get_logs():
    if logFile.exists():
        return {"log": logFile.read_text()}
    return {"log": ""}