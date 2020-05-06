import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'born'
email['to'] = 'example@gmail.com'
email['subject'] = 'youre new'

email.set_content('learning python')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('example@gmail.com', 'password')
    smtp.send_message(email)
    print('all good')