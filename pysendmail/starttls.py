import smtplib, ssl

from getpass import getpass


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "sendemailpy@gmail.com"
receiver_email = input("Enter receiver address: ")
password = getpass("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
