import smtplib

sender = 'lukasmakera@gmail.com'
receiver = 'lukasmakera1@gmail.com'
password = 'Moin123wef45'
subject = 'Python email test'
body = 'i wrote an email using python :)'

message = f"""From: Me{sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP('smtp.googlemail.com', 587)
server.starttls()

try:
    server.login(sender, password)
    print('Logged in...')
    server.sendmail(sender, receiver, message)
    print('Email has been sent')
except smtplib.SMTPAuthenticationError:
    print('Unable to sign in')