import smtplib

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('vishrutss@gmail.com','hprqmhjhspaszzxa')

    subject='Product key'
    body='1234'
    msg= f'Subject: {subject}\n\n{body}'

    smtp.sendmail('vishrutss@gmail.com','vishrutss@gmail.com',msg)
