# PDF_Converter
A Python & Streamlit web app to convert native and scanned PDFs to editable Word (.docx) files using OCR.

📄 PDF to Word Converter with OCR
A simple yet powerful web application built with Python and Streamlit to convert PDF files into editable Microsoft Word documents (.docx). This tool handles both native (text-based) and scanned (image-based) PDFs by integrating Google's Tesseract OCR engine.

✨ Features
Dual Mode Conversion: Seamlessly processes both native and scanned PDFs.

OCR Integration: Automatically detects image-based pages and applies Optical Character Recognition (OCR) to extract text.

Layout Preservation: Preserves basic paragraph structure from the original PDF.

Image Extraction: Extracts and embeds images from the PDF into the Word document.

Simple Web UI: Easy-to-use interface powered by Streamlit for uploading files and downloading results.

Clean Architecture: The core conversion logic is decoupled from the user interface for better maintainability.

🛠️ Installation & Setup
To run this application locally, you need to have Python, the Tesseract-OCR engine, and several Python libraries installed.

1. Prerequisites
Python 3.8+: Make sure you have a modern version of Python installed.

Tesseract-OCR Engine: This is crucial for converting scanned documents.

Windows: Download and run the installer from the Tesseract at UB Mannheim page. Important: During installation, make sure to check the option to add Tesseract to your system's PATH.

macOS: Use Homebrew: brew install tesseract

Linux (Debian/Ubuntu): Use apt: sudo apt-get install tesseract-ocr