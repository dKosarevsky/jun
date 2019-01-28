import smtplib, ssl

from getpass import getpass


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sendemailpy@gmail.com" # Or use input
receiver_email = input("Enter receiver address: ")
password = getpass("Type your password and press enter: ", stream=None)
message = """\
Subject: Hi there


This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
