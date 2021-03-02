import smtplib, ssl  # smtplib is the built-in Python SMTP protocol client that allows us to connect to our email account and send mail via SMTP.
from email.mime.text import MIMEText  # MIME (Multipurpose Internet Mail Extensions) is a standard for formatting files to be sent over the internet so they can be viewed in a browser or email application.
# from email.mime.base import MimeBase
import datetime
import logging

logging.basicConfig(filename='email.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')

def send_email():
    logging.info("[def send_email][sending email: start]")
    sender = "maria.clouddev@gmail.com"
    receiver = "maria.kononevs@gmail.com"
    body_of_email = "BODY OF MY EMAIL"

    # creating message
    logging.info("[def send_email][creating message]")
    msg = MIMEText(body_of_email, "html")
    msg["Subject"] = "Subject line goes here"
    msg["From"] = sender
    msg["To"] = "receiver"

        # sending message
    try:
        logging.info("[def send_email][sending message]")
        server = servermtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
        server.login(user = "maria.clouddev@gmail.com", password = "#######")
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        logging.info(f"Email not sent, error : {e}")
        logging.info("[def send_email][sending email: end]")

# send_email()

# def write_to_file(SOME INFO):

#     now = datetime.datetime.now()
#     date_formatted = now.strftime("%Y-%m-%d %H:%M:%S") # formatting time into YMD, H:M:S

#     try:
#         with open("job_offers.txt", "a+") as myfile:
#             myfile.write('Some text' + SOME INFO from parameters + date_formatted)
#             print(f"File updated on {date_formatted}")
#     except Exception as e:
#         logging.info(f"File not written, error: {e}")

