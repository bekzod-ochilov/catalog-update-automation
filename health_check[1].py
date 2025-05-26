#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails

def check_cpu_usage(): return psutil.cpu_percent(1) < 80
def check_disk_space(): return shutil.disk_usage("/").free / shutil.disk_usage("/").total * 100 > 20
def check_memory(): return psutil.virtual_memory().available / 1024 / 1024 > 100
def check_hostname(): return socket.gethostbyname("localhost") == "127.0.0.1"

def send_alert(subject):
    msg = emails.generate_email("automation@example.com", "student@example.com", subject, 
        "Please check your system and resolve the issue as soon as possible.", None)
    emails.send_email(msg)

if not check_cpu_usage():
    send_alert("Error - CPU usage is over 80%")
elif not check_disk_space():
    send_alert("Error - Available disk space is less than 20%")
elif not check_memory():
    send_alert("Error - Available memory is less than 100MB")
elif not check_hostname():
    send_alert("Error - localhost cannot be resolved to 127.0.0.1")