import smtplib
import credentials
import datetime
from twilio.rest import Client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = credentials.fromaddr
password = credentials.pwd


def mail(vehicle, path, toll_plaza):
    with smtplib.SMTP('smtp.gmail.com', 587)as smtp:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = fromaddr
        msg['Subject'] = "FasTAG protocol violation"
        body = "The vehicle '{v}' is found to have an improper FasTAG\n crossed {tp} toll plazza at {t}".format(
            v=vehicle, t=str(datetime.datetime.now()), tp=toll_plaza)
        msg.attach(MIMEText(body, 'plain'))
        filename = path.split('\\')[-1]
        attachment = open(path, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(fromaddr, password)
        # subject="test"
        # body="abcdefg"
        # msg= f'Subject:{subject}\n\n{body}'
        text = msg.as_string()
        smtp.sendmail(fromaddr, fromaddr, text)


def sms(num, toll_plaza,cost=None):
    account_sid = credentials.sid
    auth_token = credentials.auth_token
    client = Client(account_sid, auth_token)
    body=None
    if cost is None:
        body = 'vehicle num : {a}\ntoll plaza : {b}'.format(a=num, b=toll_plaza)
    else:
        body= 'An amount of {cost}rupees has been deducted from your Fastag wallet. \n Vehicle number:{a} \n toll plaza : {b}'.format(a=num, b=toll_plaza,cost=cost)
    message = client.messages \
        .create(
        body=body,
        from_=credentials.from_num,
        to='+919443654351'
    )


if __name__ == "__main__":
    path = r"E:\Hackerearth\Round 2\conda_tens\test_img\test7.jpg"
    mail("KL40L5577", path, "ABC123")
    sms("KL40L5577", "ABC123")
