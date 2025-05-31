import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(data):
    try:
        # Export to CSV
        csv_path = "report.csv"
        data.to_csv(csv_path, index=False)

        # Export to PDF
        pdf_path = "report.pdf"
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawString(100, 750, "Warranty Analyzer Report")
        c.drawString(100, 730, f"Total Records: {len(data)}")
        c.drawString(100, 710, f"Anomalies Detected: {len(data[data['Anomaly'] == -1])}")
        c.save()

        return {"csv": csv_path, "pdf": pdf_path}
    except Exception as e:
        raise ValueError(f"Error generating report: {e}")