import smtplib
import ssl
# from Split.settings import get_secret


def prepare_email(receiver, body):
    ctx = ssl.create_default_context()
    password = "dgmvmxosllrkbkly" # get_secret('GMAIL_PASSWORD')    # Your app password goes here
    subject = "Split Saventic - Nowa należność do uregulowania"
    sender = "saventicsplit@gmail.com"    # Your e-mail address
    body = body
    receiver = receiver  # Recipient's address
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.encode('utf-8'))
