import smtplib, ssl  # smtplib is the built-in Python SMTP protocol client that allows us to connect to our email account and send mail via SMTP.
from email.mime.text import MIMEText  # MIME (Multipurpose Internet Mail Extensions) is a standard for formatting files to be sent over the internet so they can be viewed in a browser or email application.
# from email.mime.base import MimeBase

def send_email():
    sender = "maria.kononevs@gmail.com"
    receiver = "maria.kononevs@gmail.com"
    body_of_email = "BODY OF MY EMAIL"

    msg = MIMEText(body_of_email, "html")
    msg["Subject"] = "Subject line goes here"
    msg["From"] = sender
    msg["To"] = "receiver"

    s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
    s.login(user = "maria.kononevs@gmail.com", password = "")
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

send_email()