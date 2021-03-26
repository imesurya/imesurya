import smtplib

class SendMail():
    subject = 'Zelthy assignment sample mail'
    body =  'Hi,' + ' your assignment deadline is today !!' + '\n \n Thanks & Regards \n Zelthy..'
    sender = 'surya.sunnapugunta@gmail.com'
    receiver = 'surya.sunnapugunta@gmail.com'
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receiver, body)
        print('Mail Sent')
    except:
        print("Couldn't send email")