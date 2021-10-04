import email
import quopri

def translate_last_message(email_response):
    return translate_message(list(email_response.values())[-1])

def translate_message(email_message):
    message = email.message_from_bytes(email_message[b'RFC822'])
    messageString = message.as_string().split("Filipe Deschamps Newsletter")[1]
    messageString = messageString.split("Cancelar inscr")[0]
    return quopri.decodestring(messageString).decode('utf-8')
   