import pandas as pd
import os
import csv

def readStudents(csvPath):
    df=pd.read_csv(csvPath)
    return df.to_dict(orient="records")

def logSend(name, email, status, message="", logFile=None):
    if log_file is None:
        log_file=os.path.join(os.path.dirname(__file__), "..", "logs", "send_log.csv")
    header=["name", "email", "status", "message"]
    exist=os.path.exists(log_file)
    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer=csv.writer(f)
        if not exist:
            writer.writerow(header)
        writer.writerow([name, email, status, message])
