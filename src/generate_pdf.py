from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import os

output_dir=os.path.join(os.path.dirname(__file__), "..", "output", "reports")
os.makedirs(output_dir, exist_ok=True)

def generate_report(student: dict) -> str:
    filename=f"{student['name'].replace(' ', '_'
    )}_report.pdf"
    path=os.path.join(output_dir, filename)
    
    c=canvas.Canvas(path, pagesize=A4)
    
    width, height=A4