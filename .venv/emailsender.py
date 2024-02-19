import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html = Template(Path("./index.html").read_text())
email = EmailMessage()
email["From"] = "Bro Bin"
email["To"] = "vieri21bin@gmail.com"
email["Subject"] = "Your Bro Bin Likes Your Tutoring"
email.set_content(html.substitute(name="TinTin"),"html")
with smtplib.SMTP(host="smtp.gmail.com",port=587) as server:
    server.ehlo()
    server.starttls()
    server.login("tutoringbybro.bin@gmail.com","kzwo odxn zmhd qans")
    server.send_message(email)
    print("Email sent")