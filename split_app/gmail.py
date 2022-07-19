import smtplib
import ssl
from Split.settings import get_secret

ctx = ssl.create_default_context()
password = get_secret('GMAIL_PASSWORD')    # Your app password goes here
sender = "saventicsplit@gmail.com"    # Your e-mail address
receiver = "bartlomiej.bruzdowski@saventic.com"  # Recipient's address
message = """
Hello Dawid.
"""

with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)