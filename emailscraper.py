import imaplib
import email
import pandas as pd

# IMAP server credentials
IMAP_SERVER = 'imap.gmail.com'
USERNAME = 'mailbot12e@gmail.com'
PASSWORD = 'guvx ncel bvrf ypdy'

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(USERNAME, PASSWORD)

# Select the mailbox (e.g., 'INBOX')
mail.select('INBOX')

# Search for emails
status, data = mail.search(None, 'ALL')
email_ids = data[0].split()

# Initialize lists to store body and headline data
bodies = []
headlines = []

# Loop through email IDs and fetch email bodies and headlines
for email_id in email_ids:
    status, data = mail.fetch(email_id, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Extract email body
    body = ""
    if email_message.is_multipart():
        for part in email_message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

    else:
        body = email_message.get_payload(decode=True).decode()
    
    bodies.append(body)

    # Extract email headline
    headline = email_message['Subject']
    headlines.append(headline)

# Create a DataFrame from the collected data
data = {'Headline': headlines, 'Body': bodies}
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv('email_data.csv', index=False)

# Logout from the IMAP server
mail.logout()
