import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the email server settings
SMTP_SERVER = 'mtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_password'

# Define the email recipients
TO_EMAILS = ['team_member1@example.com', 'team_member2@example.com']

# Define the email subject and body
SUBJECT = 'Weekly Report'
BODY = '''
Dear Team,

Here is the weekly report:

* Task 1: Completed
* Task 2: In progress
* Task 3: Delayed

Best,
Your Name
'''

# Create the email message
msg = MIMEMultipart()
msg['From'] = FROM_EMAIL
msg['To'] = ', '.join(TO_EMAILS)
msg['Subject'] = SUBJECT

# Add the email body
msg.attach(MIMEText(BODY, 'plain'))

# Connect to the email server
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(FROM_EMAIL, PASSWORD)

# Send the email
server.sendmail(FROM_EMAIL, TO_EMAILS, msg.as_string())
server.quit()

print('Email sent successfully!')