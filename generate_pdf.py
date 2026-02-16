#!/usr/bin/env python3
"""
Simple script to convert the HTML resume to PDF using weasyprint.

Install requirements:
pip install weasyprint

Usage:
python generate_pdf.py
"""

import os
from pathlib import Path

def generate_pdf():
    try:
        from weasyprint import HTML, CSS
        
        # Get the directory of this script
        script_dir = Path(__file__).parent
        html_file = script_dir / "Resume_PDF_Ready.html"
        pdf_file = script_dir / "George_Strauch_Resume.pdf"
        
        if not html_file.exists():
            print(f"Error: {html_file} not found")
            return False
        
        # Convert HTML to PDF
        HTML(filename=str(html_file)).write_pdf(str(pdf_file))
        print(f"✅ PDF generated successfully: {pdf_file}")
        return True
        
    except ImportError:
        print("❌ weasyprint not installed. Install with: pip install weasyprint")
        print("Alternative: Open Resume_PDF_Ready.html in browser and use Print to PDF")
        return False
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return False

if __name__ == "__main__":
    generate_pdf()