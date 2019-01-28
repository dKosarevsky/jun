Python comes with the built-in smtplib module for sending emails using the Simple Mail Transfer Protocol (SMTP). smtplib uses the RFC 821 protocol for SMTP. The examples in this tutorial will use the Gmail SMTP server to send emails, but the same principles apply to other email services. Although the majority of email providers use the same connection ports as the ones in this tutorial, you can run a quick Google search to confirm yours.

To get started with this tutorial, set up a Gmail account for development, or set up an SMTP debugging server that discards emails you send and prints them to the command prompt instead. Both options are laid out for you below. A local SMTP debugging server can be useful for fixing any issues with email functionality and ensuring your email functions are bug-free before sending out any emails.


python -m smtpd -c DebuggingServer -n localhost:1025


https://realpython.com/python-send-email/


About sendgrid.py:
To run this code, you must first:
Sign up for a (free) Sendgrid account
Request an API key for user validation
Add your API key by typing setx SENDGRID_API_KEY "YOUR_API_KEY" in Command Prompt (to store this API key permanently) or set SENDGRID_API_KEY YOUR_API_KEY to store it only for the current client session
More information on how to set up Sendgrid for Mac and Windows can be found in the repository’s README on Github.



Enjoy sending emails with Python, and remember: no spam please! =)
