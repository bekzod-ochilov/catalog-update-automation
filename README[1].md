# Catalog Update Automation

This project automates the process of updating a fruit catalog website using image and text data from a supplier. Built using Python, it performs:

- 📷 Image conversion (TIFF ➝ JPEG, resized)
- 📤 Uploading JPEGs to a Django server
- 📄 Parsing `.txt` descriptions into JSON and uploading via POST
- 🧾 Generating a PDF report of all processed items
- 📧 Sending the report by email
- 🩺 System health monitoring with alert emails

## Tech Used

- Python 3
- Pillow (PIL)
- ReportLab
- Requests
- psutil
- SMTP for email