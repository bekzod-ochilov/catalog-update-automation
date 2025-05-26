#!/usr/bin/env python3
import os
import datetime
import reports
import emails

desc_path = "/home/student/supplier-data/descriptions"
body = ""
for file in os.listdir(desc_path):
    if file.endswith(".txt"):
        with open(os.path.join(desc_path, file)) as f:
            lines = f.read().splitlines()
            body += f"name: {lines[0]}<br/>weight: {lines[1]}<br/><br/>"

title = "Processed Update on " + datetime.date.today().strftime("%B %d, %Y")
reports.generate_report("/tmp/processed.pdf", title, body)

email = emails.generate_email("automation@example.com", "student@example.com", 
    "Upload Completed - Online Fruit Store",
    "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
    "/tmp/processed.pdf")
emails.send_email(email)