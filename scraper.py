# imports
import imaplib, email

user = 'USER' # USERNAME AND PASSWORD REDACTED FOR PRIVACY
password = 'PASS'
imap_url = 'imap.gmail.com'

# get email content
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
    
# get key value pair
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

# get emails
def get_emails(result_bytes):
    msgs = [] # array of data
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.appened(data)

    return msgs

# SSL connection with gmail
con = imaplib.IMAP4_SSL(imap_url)

# login
con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)

# gather email
con.select('Inbox')
msgs = get_emails(search('FROM', 'REDACTED FOR PIRVACY', con))

# Calendar code redacted for privacy


