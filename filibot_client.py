from imapclient import IMAPClient
import os

def get_email_client():
    server = IMAPClient('imap.gmail.com', use_uid=True, ssl=True)
    server.login(os.getenv("EMAIL_LOGIN"), os.getenv("EMAIL_PASSWORD"))
    return server