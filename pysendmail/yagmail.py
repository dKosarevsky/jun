import yagmail

receiver = "your@gmail.com"
body = "Hello there from Yagmail"
filename = "test.pdf"

yag = yagmail.SMTP("my@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
)