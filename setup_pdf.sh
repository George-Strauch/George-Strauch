#!/bin/bash

echo "Setting up PDF generation for resume..."

# Check if pip is available
if ! command -v pip &> /dev/null; then
    echo "❌ pip not found. Please install Python and pip first."
    exit 1
fi

# Install weasyprint for PDF generation
echo "📦 Installing weasyprint..."
pip install weasyprint

# Check if installation was successful
if python -c "import weasyprint" &> /dev/null; then
    echo "✅ weasyprint installed successfully"
    echo "🚀 You can now run: python generate_pdf.py"
else
    echo "❌ weasyprint installation failed"
    echo "💡 Alternative: Open Resume_PDF_Ready.html in browser and use Print to PDF"
fi

echo ""
echo "📋 Available resume formats:"
echo "  - README.md (GitHub profile)"
echo "  - Resume.md (Detailed markdown)"
echo "  - Resume_ATS.md (ATS-friendly)"
echo "  - Resume_PDF_Ready.html (PDF conversion ready)"
echo "  - generate_pdf.py (PDF generation script)"